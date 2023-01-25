import sys


# class num
class NUM:
    # constructor, initialize all variables
    def __init__(self, at = 0, txt = ""):
        self.at = at
        self.txt = txt
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = sys.maxsize
        self.hi = -sys.maxsize
        self.w = 0
        if '-' in self.txt:
            self.w = -1
        else:
            self.w = 1

    # Add n and update values required for standard deviation
    def add(self, n):
        if n != '?':
            self.n += 1
            d = n - self.mu
            self.mu += d / self.n
            self.m2 += d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    # Return mean
    def mid(self,x=0):
        return self.mu

    # Return standard deviation using Welford's Aglorithm
    def div(self,x=0):
        # return (self.m2 < 0 or self.n < 2) and 0 or (self.m2 / (self.n - 1)) ** 0.5
        if self.m2 < 0 or self.n < 2:
            return 0
        else:
            return (self.m2 / (self.n - 1)) ** 0.5
        
    def rnd(self,x=0,n=0):
        if x=='?':
            return x
        else:
            return rnd(x,n)
