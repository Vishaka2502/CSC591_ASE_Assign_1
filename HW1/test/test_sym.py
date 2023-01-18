from HW1.src.sym import SYM
from HW1.src.utils import rnd


def test_sym():
    sym = SYM()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == rnd(sym.div())


if __name__ == "__main__":
    assert test_sym()
