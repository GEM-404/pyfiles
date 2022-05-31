#! /usr/bin/env/python3
# @author -> GEM-404 | EPHANTUS MACHARIA

"""

This module is like the terminal man command, but for
python3 modules and classes... Whenever I wanna see what
a certain module does, or how to use it, I will be using
this pyman $module to see how it works.
"""

import importlib
import sys


def main() -> str | None:
    if len(sys.argv) >= 2:
        module = sys.argv[1]
        try:
            mod = importlib.import_module(module)
            return help(mod)

        except:
            return f"Module {module} not found!!! Check {module} is installed"

    else:

        msg = "Please provide a module to look into"
        print(msg)


if __name__ == '__main__':
    main()
