#! /usr/bin/env/python3
#@author -> GEM-404 | EPHANTUS MACHARIA

"""

This module is like the terminal man command, but for
python3 modules and classes... Whenever I wanna see what
a certain module does, or how to use it, I will be using
this pyman $module to see how it works.
"""

import sys


def main():
    if len(sys.argv) >= 2:
        help(sys.argv[1])

    else:

        msg = """
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
              """

        print(msg)


if __name__ == '__main__':
    main()
