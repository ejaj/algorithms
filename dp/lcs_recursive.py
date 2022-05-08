#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : lcs_recursive.py
@Time : 5/9/22 1:50 AM
@Desc: 
"""


def lcs(X, Y, m, n):
    """
    Longest Common Subsequence using recursive method
    :param X:
    :param Y:
    :param m:
    :param n:
    :return:
    """
    if m == 0 or n == 0:
        return 0

    if X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1),
                   lcs(X, Y, m - 1, n))


def main():
    """
    Main function for drive the code.
    :return:
    """
    X = "AGGTAB"
    Y = "GXTXAYB"
    m = len(X)
    n = len(Y)

    print("Length of LCS:", lcs(X, Y, m, n))


if __name__ == '__main__':
    main()
