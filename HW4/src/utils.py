import json
import math
import random
import re
from copy import deepcopy
from pathlib import Path
from typing import Union, List

import settings

the = settings.THE
seed = settings.SEED
help_string = settings.HELP
example_funcs = settings.EXAMPLE_FUNCS


# Numeric Operations
def rint(low: int, high: int) -> int:
    """
    Returns an integer between low to high-1
    """
    return math.floor(0.5 + random.randint(low, high - 1))


def rand(low: int, high: int) -> float:
    low, high = low or 0, high or 1
    global seed
    seed = (16807 * seed) % 2147483647
    return low + (high - low) * seed / 2147483647


def rnd(n: float, n_places=None) -> float:
    """
    Returns `n` rounded to `nPlaces`
    """
    mult = math.pow(10, n_places or 3)
    return math.floor(n * mult + 0.5) / mult


def cosine(a: float, b: float, c: float) -> (float, float):
    """
    Get x, y from a line connecting `a` to `b`
    """
    x1 = (a ** 2 + c ** 2 - b ** 2) / ((2 * c) or 1)  # might be an issue if c is 0
    x2 = max(0.0, min(1.0, x1))  # in the incremental case, x1 might be outside 0,1
    y = abs((a ** 2 - x2 ** 2)) ** .5
    return x2, y


# List Operations
def kap(t: list, func):
    """
    Maps `func`(k,v) over list `t` (skip nil results)
    """
    u = {}
    for k, v in enumerate(t):
        v, k = func(k, v)
        # here unlike `#u` in lua that gives the index of last entry, +1 is not required with len(u)
        u[k or len(u)] = v
    return u


def keys(t: dict) -> list:
    """
    Returns sorted order of the keys of dict `t`
    """
    return sorted(list(t.keys()))


def push(t: list, x: any) -> any:
    """
    Pushes `x` to end of list `t`
    :return: x
    """
    t.append(x)
    return x


def any(t: list) -> any:
    """
    Returns any one item at random from given list `t`
    """
    return t[rint(0, len(t) - 1)]


def many(t: list, n: int) -> list:
    """
    Returns some items from `t`
    :param t: list
    :param n: integer specifying number of values to be return
    :return: list of `n` random values from list `t`
    """
    u = []
    for _ in range(1, n + 1):
        u.append(any(t))
    return u


def copy(t: Union[dict, list]) -> Union[dict, list]:
    """Returns deep copy"""
    return deepcopy(t)


# String Operations
def o(t) -> str:
    """
    Returns string representation of `t` where keys are in ascending order.
    """
    if not isinstance(t, dict):
        return str(t)
    return dict(sorted(t.items())).__repr__()


def oo(t: any) -> any:
    """
    Prints `t` then return it
    """
    print(o(t))
    return t


def coerce(s: str) -> any:
    """
    Return int or float or bool or string from `s`
    """
    if s.lower() == "true":
        return True
    if s.lower() == "false":
        return False
    if s.isdigit():
        return int(s)
    if s.replace('.', '').isdigit():
        return float(s)
    return s


def csv(s_filename: str, func) -> None:
    """
    Calls `func` on rows (after coercing cell text)
    """
    s_file = Path(s_filename)
    if not s_file.exists():
        print(f"File path {s_file.absolute()} doesn't exist")
        return None
    if not s_file.suffix == '.csv':
        print(f"File {s_file.absolute()} is not CSV type")
        return None

    t = []
    with open(s_file.absolute(), 'r') as file:
        for _, line in enumerate(file):
            row = list(map(coerce, line.strip().split(',')))
            t.append(row)
            func(row)


# Miscellaneous Operations
def dofile(file: str) -> dict:
    """
    Loads the file
    :param file: file name to be read
    :return:
    """
    file = open(file, "r", encoding="utf-8")
    text = (
        re.findall(r'(?<=return )[^.]*', file.read())[0]
        .replace('{', '[')
        .replace('}', ']')
        .replace('=', ':')
        .replace('[\n', '{\n')
        .replace(' ]', ' }')
        .replace('\'', '"')
        .replace('_', '"_"')
    )
    file.close()
    print("----", text)
    return json.loads(re.sub(r"(\w+):", r'"\1":', text)[:-2] + "}")


def rep_cols(cols, data: 'DATA') -> 'DATA':
    cols = copy(cols)
    for col in cols:
        col[len(col) - 1] = col[0] + ":" + col[len(col) - 1]
        for j in range(1, len(col)):
            col[j - 1] = col[j]
        col.pop()
    first_col = ['Num' + str(k) for k in range(len(cols[0]))]
    cols.insert(0, first_col)
    cols[0][len(cols) -1] = 'thingX'
    print("****", cols)
    return data(cols)


def rep_rows(t, data: 'DATA', rows: List['ROW']) -> 'DATA':
    rows = copy(rows)
    for j, s in enumerate(rows[-1]):
        rows[0][j] = rows[0][j] + ":" + s
    rows.pop()
    for n, row in enumerate(rows):
        if n == 0:
            row.append('thingX')
        else:
            u = t['rows'][-n]
            row.append(u[-1])
    return data(rows)


def rep_place(data: 'DATA') -> None:
    n = 20
    g = [[' ' for _ in range(n + 1)] for _ in range(n + 1)]
    maxy = 0
    print('')
    for r, row in enumerate(data.rows):
        c = chr(64 + r)
        print(c, row.cells[-1])
        x, y = row.x * n // 1, row.y * n // 1
        maxy = int(max(maxy, y + 1))
        g[y + 1][x + 1] = c
    print('')
    for y in range(1, maxy + 1):
        print(' '.join(g[y]))


def transpose(t):
    u = []
    for i in range(len(t[1])):
        u.append([])
        for j in range(len(t)):
            u[i].append(t[j][i])
    return u


def rep_grid(source_file: str, data: 'DATA') -> None:
    t = dofile(source_file)
    rows = rep_rows(t, data, transpose(t['cols']))
    cols = rep_cols(t['cols'], data)
    show(rows.cluster(), "mid", rows.cols.all, 1)
    show(cols.cluster(), "mid", cols.cols.all, 1)
    rep_place(rows)


def show(node, what: str = 'mid', cols: List[Union['Num', 'Sym']] = None, n_places: int = 1, lvl: int = 0) -> None:
    """
    Prints the tree
    :param node: Node of tree
    :param what: str: Statistics to print
    :param cols: list: Columns to print stats for
    :param n_places: int: Number of decimals to round the values to
    :param lvl: int: Level in the tree (default = 0)
    """
    if node:
        print('| ' * lvl + str(len(node['data'].rows)) + '  ', end='')
        if not node.get('left') or lvl == 0:
            print(node['data'].stats('mid', node['data'].cols.y, n_places))
        else:
            print('')
        show(node.get('left'), what, cols, n_places, lvl + 1)
        show(node.get('right'), what, cols, n_places, lvl + 1)


def example(key: str, text: str, fun) -> None:
    """
    Update the help string with actions passed as key, text and func
    """
    example_funcs[key] = fun
    global help_string
    help_string = f"""{help_string} -g {key} \t {text} \n"""
