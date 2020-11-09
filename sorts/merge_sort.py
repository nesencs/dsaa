#!/usr/bin python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 上午8:29
# @Author  : nobody
# @Site    : 
# @File    : merge_sort.py
# @Software: PyCharm


def merge_sort(data):
    """

    :param data:
    :return:

    >>> merge_sort([3,4,5,2,1])
    [1, 2, 3, 4, 5]

    """
    if len(data) < 2:
        return data

    def _merge(left, right):
        def meg():
            while left and right:
                yield (left if left[0] < right[0] else right).pop(0)

            yield from left
            yield from right

        return list(meg())

    mid = len(data) // 2
    return _merge(merge_sort(data[0:mid]), merge_sort(data[mid:]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    a = [3, 2, 4, 5, 1]
    print(merge_sort(a))
