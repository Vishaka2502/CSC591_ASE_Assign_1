from HW3.src import utils
from HW3.src.data import DATA
from HW3.src.num import NUM
from HW3.src.sym import SYM
from HW3.src.utils import rnd, oo, the, rand, csv, show

n = 0


def test_the():
    r = oo(the)
    return r


def test_rand():
    num1, num2 = NUM(), NUM()
    utils.seed = the['seed']
    for i in range(1, 11):
        num1.add(rand(0, 1))

    utils.seed = the['seed']
    for i in range(1, 11):
        num2.add(rand(0, 1))

    m1, m2 = rnd(num1.mid(), 10), rnd(num2.mid(), 10)
    return m1 == m2 and .5 == rnd(m1, 1)


def test_sym():
    sym = SYM()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == rnd(sym.div())


def test_num():
    num = NUM()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    return 11 / 7 == num.mid() and 0.787 == rnd(num.div())


def test_csv():
    def func(t):
        global n
        n += len(t)

    csv(the['file'], func)
    return n == 8 * 399


def test_data():
    data = DATA(the['file'])
    return len(data.rows) == 398 and \
           data.cols.y[0].w == -1 and \
           data.cols.x[1].at == 1 and \
           len(data.cols.x) == 4


def test_stats():
    data = DATA(the['file'])
    for k, cols in {'y': data.cols.y, 'x': data.cols.x}.items():
        print(k, 'mid', data.stats('mid', cols, 2))
        print('', 'div', data.stats('div', cols, 2))
    return True


def test_clone():
    data1 = DATA(the['file'])
    data2 = data1.clone(data1.rows)
    return len(data1.rows) == len(data2.rows) and \
           data1.cols.y[1].w == data2.cols.y[1].w and \
           data1.cols.x[1].at == data2.cols.x[1].at and \
           len(data1.cols.x) == len(data2.cols.x)


def test_around():
    data = DATA(the['file'])
    print(0, '\t', 0, '\t', data.rows[0].cells)
    for n, t in enumerate(data.around(data.rows[0])):
        if ((n + 1) % 50) == 0:
            print(n + 1, '\t', rnd(t['dist'], 2), '\t', t['row'].cells)


def test_half():
    data = DATA(the['file'])
    left, right, A, B, mid, c = data.half()
    print(len(left), len(right), len(data.rows))
    print(A.cells, c)
    print(mid.cells)
    print(B.cells)


def test_cluster():
    data = DATA(the['file'])
    show(data.cluster(), "mid", data.cols.y, 1)


def test_optimize():
    data = DATA(the['file'])
    show(data.sway(), 'mid', data.cols.y, 1)
