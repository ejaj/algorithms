#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : fibonacci.py
@Time : 4/24/22 4:35 PM
@Desc: 
"""


def fibonacci(n):
    """
    Fibonacci series
    :param n:
    :return:
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    """
    Main function for run code
    :return:
    """
    n = 10
    if n <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(n):
            print(fibonacci(i))


if __name__ == '__main__':
    main()
