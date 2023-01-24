import math
import random
from pathlib import Path

import settings

the = settings.THE
seed = settings.SEED
help_string = settings.HELP
example_funcs = settings.EXAMPLE_FUNCS


def rint(low: int, high: int) -> int:
    """
    Returns an integer between low to high-1
    """
    return math.floor(0.5 + random.randint(low, high-1))


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


def fmap(t: list, func):
    """
    Maps `func`(v) over list `t` (skip nil results)
    """
    u = {}
    for k, v in enumerate(t):
        v, k = func(v)
        # here unlike `#u` in lua that gives the index of last entry, +1 is not required with len(u)
        u[k or len(u)] = v
    return u


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
    push `x` to end of list `t`
    :return: x
    """
    t.append(x)
    return x


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


def example(key: str, text: str, fun) -> None:
    """
    Update the help string with actions passed as key, text and func
    """
    example_funcs[key] = fun
    global help_string
    help_string = f"""{help_string} -g {key} \t {text} \n"""


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
