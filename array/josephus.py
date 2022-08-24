"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.
For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""


def josephus(int_arr, skip):
    skip = skip - 1
    len_list = len((int_arr))
    idx = 0
    while len_list > 0:
        idx = (skip + idx) % len_list
        yield int_arr.pop(idx)
        len_list -= 1


int_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
skip = 3
generator_jose = josephus(int_arr, 3)
for i in generator_jose:
    print(i)
