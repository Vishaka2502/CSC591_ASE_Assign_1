import os
import utils
import re
import sys


options = {}
helpString = """
script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 

USAGE:   script.lua  [OPTIONS] [-g ACTION]

OPTIONS:
  -d  --dump  on crash, dump stack = false
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211

ACTIONS:
"""

def settings(pstr):
    pattern = """\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"""
    r = re.compile(pattern)
    matches = r.findall(pstr)
    for k, v in matches:
        options[k] = utils.coerce(v)
    
    return options


def cli(options):
    for key, val in options.items():
        val = str(val)
        for n, x in enumerate(sys.argv):
            if x == "-" + key[0] or x == "--" + key:
                val = val=="false" and "true" or val=="true" and "false" or n+1 <= len(sys.argv)
        options[key] = utils.coerce(val)
    return options


def main(options, help, exampleFunctions):
    saved, fails = {}, 0
    for key, val in enumerate(cli(settings(helpString))):
        options[key] = val
        saved[key] = val

    if options["help"]:
        print(helpString)    
    else:
        for what, fun in enumerate(exampleFunctions):
            if options["go"] == "all" or what == options["go"]:
                for k,v in enumerate(saved):
                    options[k] = v
                optseed = options["seed"]
                if not exampleFunctions[what]():
                    fails += 1
                    print("❌ fail:",what)
                else:
                    print("✅ pass:",what)

    os.exit(fails)


if __name__ == '__main__':
    # main({}, helpString, )
    print(cli(settings(helpString)))
import sys

#class NUM
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
    
