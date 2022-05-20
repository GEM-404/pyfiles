#! /usr/bin/env python3
# @author -> GEM-404 || EPHANTUS MACHARIA


from sys import argv
from typing import List, TypeVar


T = TypeVar("T", float, int)


calc_ops = {
    "x": "multiply",
    "*": "multiply",
    "/": "divide",
    "+": "add",
    "-": "minus",
    "**": "power",
}


def multiply(a: T, b: T) -> T:
    return a * b


def add(a: T, b: T) -> T:
    return a + b


def minus(a: T, b: T) -> T:
    return a - b


def divide(a: T, b: T) -> float:
    return a / b


def power(a: T, b: T) -> T:
    return a ** b


def get_args():
    return str(argv[1])


def split_args(args: str):
    lst_args = list(args)
    return lst_args


def main():
    args = get_args()

    lst_args: List[str] = split_args(args)

    print(lst_args)



if __name__ == '__main__':
    main()

