import sys
from typing import Union

from HW2.src.utils import rnd


# class num
class NUM:
    # constructor, initialize all variables
    def __init__(self, at: int = 0, txt: str = "") -> None:
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

    def add(self, n: Union[float, str]) -> None:
        """
        Add n and update values required for standard deviation
        :param n: Union[float, str]:
        """
        if n != '?':
            self.n += 1
            d = n - self.mu
            self.mu += d / self.n
            self.m2 += d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self) -> float:
        """
        Get mean
        :return: float: mean value
        """
        return self.mu

    def div(self) -> float:
        """
        Get standard deviation using Welford's Aglorithm
        :return: float: standard deviation
        """
        # return (self.m2 < 0 or self.n < 2) and 0 or (self.m2 / (self.n - 1)) ** 0.5
        if self.m2 < 0 or self.n < 2:
            return 0
        else:
            return (self.m2 / (self.n - 1)) ** 0.5

    @staticmethod
    def rnd(x: Union[float, str], n: int) -> Union[float, str]:
        """
        Get a rounded number if a value else return the str '?'
        :param x: Union[float, str]: number to be rounded
        :param n: int: rounded over to `n` places
        :return: Union[float, str]: rounded value or missing value symbol (?)
        """
        if x == '?':
            return x
        else:
            return rnd(x, n)
