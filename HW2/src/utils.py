import math
import random

from HW1 import settings

the = settings.THE
seed = settings.SEED
help_string = settings.HELP
example_funcs = settings.EXAMPLE_FUNCS


def rint(low, high):
    return math.floor(0.5 + random.randint(low, high-1))


def rand(low, high):
    low, high = low or 0, high or 1
    global seed
    seed = (16807 * seed) % 2147483647
    return low + (high - low) * seed / 2147483647


def rnd(n, n_places=None):
    mult = math.pow(10, n_places or 3)
    return math.floor(n * mult + 0.5) / mult


def fmap(t, func):
    u = {}
    for k, v in t.items():
        v, k = func(v)
        u[k or (1+len(u))] = v
    return u


def kap(t, func):
    u = {}
    for k, v in t.items():
        v, k = func(k, v)
        u[k or 1+len(u)] = v
    return u


def tsort(t):
    t = dict(sorted(t.items()))
    return t


def o(t):
    if not isinstance(t, dict):
        return str(t)
    return tsort(t).__repr__()


def oo(t):
    print(o(t))
    return t


def coerce(s):
    if s.lower() == "true":
        return True
    if s.lower() == "false":
        return False
    if s.isdigit():
        return int(s)
    if s.replace('.', '').isdigit():
        return float(s)
    return s


def example(key, text, fun):
    example_funcs[key] = fun
    global help_string
    help_string = f"""{help_string} -g {key} \t {text} \n"""
