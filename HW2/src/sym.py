import math
from typing import Union


class SYM:
    # constructor, initialize all variables
    def __init__(self, at: int = 0, txt: str = ""):
        self.at = at    # column position
        self.txt = txt  # column name
        self.n = 0
        self.has = dict()
        self.most = 0
        self.mode = None

    def add(self, x) -> None:
        """
        Update counts of things seen so far
        """
        if x != '?':
            self.n += 1
            self.has[x] = 1 + (self.has[x] if x in self.has else 0)

            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self) -> any:
        """
        Get the mode
        :return: any: mode
        """
        return self.mode

    def div(self) -> float:
        """
        Get the entropy
        :return: float: entropy
        """
        def fun(p):
            return p * math.log(p, 2)

        e = 0
        for _, n in self.has.items():
            e = e + fun(n / self.n)
        return -e

    @staticmethod
    def rnd(x: Union[float, str]) -> Union[float, str]:
        """
        Return number unchanged (SYMs do not get rounded)
        :param x: Union[float, str]: number or missing value symbol (?)
        :return: Union[float, str]: return the parameter unchanged
        """
        return x
