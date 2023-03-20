import re
import sys

from HW7.test.test_examples import *


def settings(pstr):
    table = {}
    pattern = """\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"""
    r = re.compile(pattern)
    matches = r.findall(pstr)
    for k, v in matches:
        table[k] = coerce(v)
    return table


def cli(options):
    for key, val in options.items():
        val = str(val)
        for n, x in enumerate(sys.argv):
            if x == "-" + key[0] or x == "--" + key:
                if val.lower() == 'false':
                    val = 'true'
                elif val.lower() == 'true':
                    val = 'false'
                else:
                    val = sys.argv[n + 1]
                # val = val == "false" and "true" or val == "true" and "false" or sys.argv[n+1]
        options[key] = coerce(val)
    return options


def main():
    saved, fails, success, options = {}, 0, 0, the
    for key, val in cli(settings(help_string)).items():
        options[key] = val
        saved[key] = val

    if options["help"]:
        print(help_string)
    else:
        for what, fun in example_funcs.items():
            if options["go"] == "all" or what == options["go"]:
                for k, v in saved.items():
                    options[k] = v
                global seed
                seed = options["seed"]
                print('\n▶️ ', what, ("-") * (60))
                if example_funcs[what]() == False:
                    fails += 1
                    print("❌ fail:", what)
                else:
                    success += 1
                    print("✅ pass:", what)
    if success + fails > 0:
        print("🔆", {'pass': success, 'fail': fails, 'success': 100 * success / (success + fails) // 1})
    sys.exit(fails)


if __name__ == '__main__':
    example('ok', 'test ok', test_ok)
    example('sample', 'test sample', test_sample)
    example('num', 'test num', test_num)
    example('gauss', 'test gaussian', test_gauss)
    example('bootmu', 'bootstrap mu', test_bootmu)
    example('basic', 'basic test', test_basic)
    example('pre', 'pre test', test_pre)
    example('five', 'five', test_five)
    example('six', 'six', test_six)
    example('tiles', 'test tiles', test_tiles)
    example('sk', 'test sk', test_sk)
    main()
