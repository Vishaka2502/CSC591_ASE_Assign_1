import math
from typing import Union, List

from HW3.src import utils
from HW3.src.cols import COLS
from HW3.src.num import NUM
from HW3.src.row import ROW
from HW3.src.sym import SYM
from HW3.src.utils import csv, the, cosine, many, kap


class DATA:
    def __init__(self, src: any) -> None:
        self.rows = []
        self.cols = None

        if isinstance(src, str):
            csv(src, self.add)
        else:
            self.add(src or [])

    def add(self, t: Union[ROW, list]) -> None:
        """
        Adds a new row, updates column headers
        :param t: param t: Union[ROW, list]:
        :return:
        """
        if self.cols:  # true if we have already seen the column names
            t = t if isinstance(t, ROW) else ROW(t)  # t = t if t.cells else ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)  # here, we create "i.cols" from the first row

    def clone(self, init: list) -> 'DATA':
        """
        Returns a clone with the same structure
        :param init: Initial data for the clone
        :return:
        """
        data = DATA(list(self.cols.names))
        list(map(data.add, init or []))
        return data

    def stats(self, what: str = 'mid', cols=None, n_places: int = 0) -> (Union[float, str], str):
        """
        Reports mid or div of cols (defaults to i.cols.y)
        :param what: str: (Default value = None)
        :param cols: (Default value = None)
        :param n_places: int: (Default value = 0)
        :return: tuple(Union[float, str], str)
        """

        def fun(_, col):
            val = getattr(col, what)()
            return col.rnd(val, n_places), col.txt

        return kap(cols or self.cols.y, fun)

    def better(self, row1: ROW, row2: ROW) -> bool:
        """
        Returns true if `row1` dominates (via Zitzler04)
        :param row1: ROW
        :param row2: ROW
        :return: bool: true if row1 dominates
        """
        s1, s2 = 0, 0
        ys = self.cols.y
        for col in ys:
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x - y) / len(ys))
            s2 = s2 - math.exp(col.w * (y - x) / len(ys))
        return s1 / len(ys) < s2 / len(ys)

    def dist(self, row1: ROW, row2: ROW, cols: List[Union[NUM, SYM]] = None) -> float:
        """
        Returns distance between the two rows
        :param row1: ROW
        :param row2: ROW
        :param cols: List[Union[NUM, SYM]]
        :return: float: returns 0..1 distance `row1` to `row2`
        """
        n, d = 0, 0
        for col in cols or self.cols.x:
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at]) ** the['p']
        return (d / n) ** (1 / the['p'])

    def around(self, row1: ROW, rows: List[ROW] = None, cols: List[Union[NUM, SYM]] = None) -> List[dict]:
        """
        Sorts other `rows` by distance to `row1`
        :param row1: ROW
        :param rows: List[ROW]
        :param cols: List[Union[NUM, SYM]]
        :return: List of dictionary with distances of each row from `row1`
        """

        def func(row2):
            return {'row': row2, 'dist': self.dist(row1, row2, cols)}

        return sorted(list(map(func, rows or self.rows)), key=lambda x: x['dist'])

    def half(self, rows: List[ROW] = None, cols: List[Union[NUM, SYM]] = None,
             above: ROW = None) -> (list, list, ROW, ROW, ROW, float):
        """
        Divides data using 2 far points
        """

        def dist(row1, row2):
            return self.dist(row1, row2, cols)

        def project(row):
            return {'row': row, 'dist': cosine(dist(row, A), dist(row, B), c)}

        rows = (rows if rows else self.rows)
        some = many(rows, the['Sample'])
        A = above if above else utils.any(some)
        B = self.around(A, some)[int(the['Far'] * len(rows)) // 1]['row']
        c = dist(A, B)
        left = []
        right = []

        for n, tmp in enumerate(sorted(list(map(project, rows)), key=lambda k: k['dist'])):
            if n < len(rows) // 2:
                left.append(tmp['row'])
                mid = tmp['row']
            else:
                right.append(tmp['row'])

        return left, right, A, B, mid, c

    def cluster(self, rows: List[ROW] = None, minimum: int = None, cols: List[Union[NUM, SYM]] = None,
                above: ROW = None) -> dict:
        """
        Get `rows`, recursively halved
        :param rows:
        :param minimum:
        :param cols:
        :param above:
        :return:
        """
        rows = rows or self.rows
        cols = cols or self.cols.x
        minimum = minimum if minimum else len(rows) ** the['min']
        node = {'data': self.clone(rows)}
        if len(rows) >= 2 * minimum:
            left, right, node['A'], node['B'], node['mid'], c = self.half(rows, cols, above)
            node['left'] = self.cluster(left, minimum, cols, node['A'])
            node['right'] = self.cluster(right, minimum, cols, node['B'])
        return node

    def sway(self, rows: List[ROW] = None, minimum: int = None, cols: List[Union[NUM, SYM]] = None,
             above: ROW = None) -> dict:
        """
        Get best half, recursively
        :param rows:
        :param minimum:
        :param cols:
        :param above:
        :return:
        """
        rows = rows or self.rows
        cols = cols or self.cols.x
        minimum = minimum if minimum else len(rows) ** the['min']
        node = {'data': self.clone(rows)}
        if len(rows) > 2 * minimum:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows, cols, above)
            if self.better(node['B'], node['A']):
                left, right, node['A'], node['B'] = right, left, node['B'], node['A']
            node['left'] = self.sway(left, minimum, cols, node['A'])
        return node
