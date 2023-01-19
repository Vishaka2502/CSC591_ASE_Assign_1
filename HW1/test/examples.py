from HW1.src.sym import SYM
from HW1.src.utils import rnd, oo, the


def test_the():
    r = oo(the)
    return r


def test_sym():
    sym = SYM()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == rnd(sym.div())
