from HW7.src.utils import *
import numpy as np


def test_ok(n=1):
    random.seed(n)


def test_sample():
    for i in range(10):
        print('', ''.join(samples(['a', 'b', 'c', 'd', 'e']).values()))


def test_num():
    n = NUM()
    for i in range(1, 11):
        n.add(i)
    print('', n.n, n.mu, n.sd)


def test_gauss():
    t = []
    for i in range(10 ** 4):
        t.append(gaussian(10, 2))
    n = NUM()
    for i in t:
        n.add(i)
    print('', n.n, n.mu, n.sd)


def test_bootmu():
    a = [gaussian(10, 1) for i in range(100)]
    print('', '\t', 'mu', '\t', 'sd', '\t', 'cliffs', 'boot', 'both')
    print('', '\t', '--', '\t', '--', '\t', '------', '----', '----')
    for mu in np.arange(10, 11.1, 0.1):
        b = [gaussian(mu, 1) for i in range(100)]
        cl = cliffs_delta(a, b)
        bs = bootstrap(a, b)
        print('', '\t', round(mu, 2), '\t', 1, '\t', cl, bs, cl and bs)


def test_basic():
    print("\t\tTrue", bootstrap([8, 7, 6, 2, 5, 8, 7, 3],
                                [8, 7, 6, 2, 5, 8, 7, 3]),
          cliffs_delta([8, 7, 6, 2, 5, 8, 7, 3],
                       [8, 7, 6, 2, 5, 8, 7, 3]))
    print("\t\tFalse", bootstrap([8, 7, 6, 2, 5, 8, 7, 3],
                                 [9, 9, 7, 8, 10, 9, 6]),
          cliffs_delta([8, 7, 6, 2, 5, 8, 7, 3],
                       [9, 9, 7, 8, 10, 9, 6]))
    print("\t\tFalse",
          bootstrap([0.34, 0.49, 0.51, 0.6, .34, .49, .51, .6],
                    [0.6, 0.7, 0.8, 0.9, .6, .7, .8, .9]),
          cliffs_delta([0.34, 0.49, 0.51, 0.6, .34, .49, .51, .6],
                       [0.6, 0.7, 0.8, 0.9, .6, .7, .8, .9]))


def test_pre():
    print('\neg3')
    d = 1
    for i in range(10):
        t1, t2 = [], []
        for j in range(32):
            t1.append(gaussian(10, 1))
            t2.append(gaussian(d * 10, 1))
        print('\t', d, '\t', d < 1.1, '\t', bootstrap(t1, t2), '\t', bootstrap(t1, t1))
        d = round(d + 0.05, 2)


def test_five():
    for rx in tiles(scott_knot(
            [RX([0.34, 0.49, 0.51, 0.6, .34, .49, .51, .6], 'rx1'),
             RX([0.6, 0.7, 0.8, 0.9, .6, .7, .8, .9], 'rx2'),
             RX([0.15, 0.25, 0.4, 0.35, 0.15, 0.25, 0.4, 0.35], 'rx3'),
             RX([0.6, 0.7, 0.8, 0.9, 0.6, 0.7, 0.8, 0.9], 'rx4'),
             RX([0.1, 0.2, 0.3, 0.4, 0.1, 0.2, 0.3, 0.4], 'rx5')])):
        print(rx['name'], rx['rank'], rx['show'])


def test_six():
    for rx in tiles(scott_knot(
            [RX([101, 100, 99, 101, 99.5, 101, 100, 99, 101, 99.5], 'rx1'),
             RX([101, 100, 99, 101, 100, 101, 100, 99, 101, 100], 'rx2'),
             RX([101, 100, 99.5, 101, 99, 101, 100, 99.5, 101, 99], 'rx3'),
             RX([101, 100, 99, 101, 100, 101, 100, 99, 101, 100], 'rx4')])):
        print(rx['name'], rx['rank'], rx['show'])


def test_tiles():
    rxs, a, b, c, d, e, f, g, h, j, k = [], [], [], [], [], [], [], [], [], [], []
    for _ in range(1000):
        a.append(gaussian(10, 1))
    for _ in range(1000):
        b.append(gaussian(10.1, 1))
    for _ in range(1000):
        c.append(gaussian(20, 1))
    for _ in range(1000):
        d.append(gaussian(30, 1))
    for _ in range(1000):
        e.append(gaussian(30.1, 1))
    for _ in range(1000):
        f.append(gaussian(10, 1))
    for _ in range(1000):
        g.append(gaussian(10, 1))
    for _ in range(1000):
        h.append(gaussian(40, 1))
    for _ in range(1000):
        j.append(gaussian(40, 3))
    for _ in range(1000):
        k.append(gaussian(10, 1))
    for k, v in enumerate([a, b, c, d, e, f, g, h, j, k]):
        rxs.append(RX(v, 'rx' + str(k + 1)))
    rxs.sort(key=lambda x: mid(x))
    for rx in tiles(rxs):
        print('', rx['name'], rx['show'])


def test_sk():
    rxs, a, b, c, d, e, f, g, h, j, k = [], [], [], [], [], [], [], [], [], [], []
    for _ in range(1000):
        a.append(gaussian(10, 1))
    for _ in range(1000):
        b.append(gaussian(10.1, 1))
    for _ in range(1000):
        c.append(gaussian(20, 1))
    for _ in range(1000):
        d.append(gaussian(30, 1))
    for _ in range(1000):
        e.append(gaussian(30.1, 1))
    for _ in range(1000):
        f.append(gaussian(10, 1))
    for _ in range(1000):
        g.append(gaussian(10, 1))
    for _ in range(1000):
        h.append(gaussian(40, 1))
    for _ in range(1000):
        j.append(gaussian(40, 3))
    for _ in range(1000):
        k.append(gaussian(10, 1))
    for k, v in enumerate([a, b, c, d, e, f, g, h, j, k]):
        rxs.append(RX(v, 'rx' + str(k + 1)))
    for rx in tiles(scott_knot(rxs)):
        print('', rx['rank'], rx['name'], rx['show'])
