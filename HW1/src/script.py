import os

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

def settings():
    pass

def cli(options):
    for key, val in enumerate(options):
        val = str(val)
        for n, x in enumerate()


def main(options, help, exampleFunctions):
    saved, fails = {}, 0
    for key, val in enumerate():
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
    main()
