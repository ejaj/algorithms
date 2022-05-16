#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : factorial.py
@Time : 4/24/22 4:07 PM
@Desc:
"""


def factorial(n):
    """
    Factorial number
    :param n:
    :return:
    """
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def main():
    """
    Main  function for drive code
    :return:
    """
    n = 5
    if n < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        print("The factorial of", n, "is", factorial(n))


if __name__ == '__main__':
    main()
