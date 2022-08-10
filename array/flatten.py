import itertools
from collections.abc import Iterable


def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for element in input_arr:
        if not isinstance(element, str) and isinstance(element, Iterable):
            flatten(element, output_arr)
        else:
            output_arr.append(element)
    return output_arr


def flatten_iter(iterable):
    for element in iterable:
        if not isinstance(element, str) and isinstance(element, Iterable):
            yield from flatten_iter(element)
        else:
            yield element
    

original_list = [
    [11, 21, 30],
    [19, 63, 71],
    [81, 99]
]
print(list(flatten_iter(original_list)))
# ans = []
# for element in original_list:
#     for value in element:
#         ans.append(value)
# print(ans)
#
# flatten_list = [value for element in original_list for value in element]
# print(flatten_list)
# flatten_list = list(itertools.chain(*original_list))
# print(flatten_list)
