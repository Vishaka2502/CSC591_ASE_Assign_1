import math


class SYM:
    # constructor, initialize all variables
    def __init__(self, at=None, txt=None):
        self.at = at or 0       # column position
        self.txt = txt or ""    # column name
        self.n = 0
        self.has = dict()
        self.most = 0
        self.mode = None

    # Update counts of things seen so far
    def add(self, x):
        if x != '?':
            self.n += 1
            self.has[x] = 1 + (self.has[x] if x in self.has else 0)

            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    # Return mode
    def mid(self):
        return self.mode

    # Return the entropy
    def div(self):
        def fun(p):
            return p * math.log(p, 2)

        e = 0
        for _, n in self.has.items():
            e = e + fun(n / self.n)
        return -e

    # Return number unchanged (SYMs do not get rounded)
    def rnd(self, x):
        return x
