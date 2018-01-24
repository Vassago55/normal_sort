# -*- coding:utf-8 -*-
import random
"""
直插排序, O(n) = n^2
"""


class StraightInsertion(object):
    def __init__(self, original_list):
        self.original_list = original_list

    def sort(self):
        length = len(self.original_list)
        for i in range(1, length):
            for j in range(0, i):
                # 与之前的有序数列依次比较
                if self.original_list[i] < self.original_list[j]:
                    self.original_list[j], self.original_list[i] = self.original_list[i], self.original_list[j]  # 改变原序列


if __name__ == '__main__':
    my_list = [random.randint(0, 100) for _ in range(0, 10)]
    print("before sort: {}".format(my_list))
    StraightInsertion(my_list).sort()
    print("after sort: {}".format(my_list))
