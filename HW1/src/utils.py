import math
import random

def rint(low, high):
    return math.floor(0.5 + random.randint(low, high-1))


def rand(low, high, seed = 937162211):
    low, high = low or 0, high or 1
    seed = (16807 * seed) % 2147483647
    return low + (high - low) * seed / 2147483647


def rnd(n, nPlaces):
    mult = math.pow(10, nPlaces or 3)
    return math.floor(n * mult + 0.5) / mult


def fmap(t, func):
    u = {}
    for k,v in enumerate(t):
        v, k = func(v)
        u[k or (1+len(u))] = v
    return u


def kap(t, func):
    u = {}
    for k,v in enumerate(t):
        v, k = func(k, v)
        u[k or 1+len(u)] = v
    return u


def tsort(t, func):
    t = dict(sorted(t.items()))
    return t


def o(t):
    if not isinstance(t, dict):
        return str(t)
    eqStr = ""
    eqStr += "{"


def oo(t):
    print(o(t))
    return t


def coerce(s):
    if isinstance(s, bool):
        return s
    if isinstance(s, int):
        return int(s)
    if isinstance(s, str):
        if s.lower() == "true":
            return True
        if s.lower() == "false":
            return False
        return s