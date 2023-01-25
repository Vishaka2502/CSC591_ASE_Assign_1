import os
import sys
import re
import utils as ut
from HW2.src.cols import COLS
from HW2.src.cols import ROW



class DATA:
    def __init__(self,src={}):
        self.row = []
        self.cols = None
        fun = lambda x: self.add(x)
        if isinstance(src, str):
            ut.csv(src, fun)  # load from a csv file on disk
        else:
            ut.map(src, fun)  # load from a list
    
    def add(self, t):
        if self.cols:
            if hasattr(t, 'cells'):
                t = t
            else:
                t = ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)
            
    def clone(self, init={}, data={}):
        data = DATA({self.cols.names})
        ut.map(init, lambda x: data.add(x))
        return data
    
    def stats(self, what=None, cols=None, nPlaces=0):
        def fun(k, col):
            return col.rnd(getattr(col)[what or "mid"](col), nPlaces), col.txt 
        return ut.kap(cols or self.cols.y, fun)
