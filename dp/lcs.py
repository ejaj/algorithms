#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : lcs.py
@Time : 5/9/22 1:42 AM
@Desc: 
"""


def lcs_algo(S1, S2, m, n):
    """
    Longest Common Subsequence using DP
    :param S1:
    :param S2:
    :param m:
    :param n:
    :return:
    """
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    index = L[m][n]
    lcs_algo = [""] * (index + 1)
    lcs_algo[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            lcs_algo[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("LCS: " + "".join(lcs_algo))


def main():
    """
    Main function for drive the code
    :return:
    """
    S1 = "ACADB"
    S2 = "CBDA"
    m = len(S1)
    n = len(S2)
    lcs_algo(S1, S2, m, n)


if __name__ == '__main__':
    main()
