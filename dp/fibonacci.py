#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : fibonacci.py
@Time : 5/9/22 11:10 AM
@Desc: 
"""


def fibonacci(n):
    """
    Fibonacci series, using dp
    :param n:
    :return:
    """
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


def main():
    """
    Main function for drive the code.
    :return:
    """
    print(fibonacci(3))


if __name__ == '__main__':
    main()
