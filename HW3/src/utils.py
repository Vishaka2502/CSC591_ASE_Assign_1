import math
import random
from pathlib import Path

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
def show(node, what: str, cols: list, n_places: int, lvl: int = 0) -> None:
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
