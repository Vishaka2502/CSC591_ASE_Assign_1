from typing import Union

from HW2.src.cols import COLS
from HW2.src.row import ROW
from HW2.src.utils import csv


class DATA:
    def __init__(self, src: any) -> None:
        self.rows = []
        self.cols = None

        if isinstance(src, str):
            csv(src, self.add)
        else:
            map(self.add, src or [])

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

    def clone(self, init=[]):
        data = DATA(self.cols.names)
        map(lambda x: data.add(x), init)
        return data

    def stats(self, what: str = None, cols=None, n_places: int = 0) -> (Union[float, str], str):
        """
        Reports mid or div of cols (defaults to i.cols.y)
        :param what: str: (Default value = None)
        :param cols: (Default value = None)
        :param n_places: int: (Default value = 0)
        :return: tuple(Union[float, str], str)
        """
        def fun(col):
            val = getattr(col, what or "mid")(col)
            return col.rnd(val, n_places), col.txt

        return map(fun, cols or self.cols.y)
