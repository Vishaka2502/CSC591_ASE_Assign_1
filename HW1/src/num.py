
import sys
import math
import os
import utils

#class num
class NUM:
    #constructor, initialize all variables
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = sys.maxsize
        self.hi = -sys.maxsize
    
    #Add n and update values required for standard deviation
    def add(self, n):
        if n!='?':
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + d/(self.n)
            self.m2 = self.m2 + d*(n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)
    
    #Return mean
    def mid(self,x):
        return self.mu
    
    #Return standard deviation using Welford's Aglorithm
    def div(self,x):
        return ((self.m2 <0 or self.n < 2) and 0 or (self.m2/(self.n-1))**(0.5))
        if self.m2 < 0 or self.n < 2:
            return 0
        else:
            return (self.m2 / (self.n - 1)) ** 0.5
