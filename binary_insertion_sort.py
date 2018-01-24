# -*- coding: utf-8 -*-
import random
"""
折半插入排序 O(n) = n^2
"""


class BinaryInsertion(object):
    def __init__(self, original_list):
        self.original_list = original_list

    def sort(self):
        length = len(self.original_list)
        for i in range(1, length):
            self.binary(start=0, end=i-1, current=i)

    def binary(self, start, end, current):
        cursor = int((end + start) / 2) if end != start else end
        if (end == start) or (cursor == 0) or (self.original_list[current] == self.original_list[cursor]):
            if self.original_list[current] >= self.original_list[cursor]:
                self.original_list.insert(cursor+1, self.original_list[current])
            else:
                self.original_list.insert(cursor, self.original_list[current])
            del self.original_list[current+1]
        elif self.original_list[current] > self.original_list[cursor]:
            self.binary(cursor+1, end, current)
        elif self.original_list[current] < self.original_list[cursor]:
            self.binary(start, cursor-1, current)


if __name__ == '__main__':
    my_list = [random.randint(0, 100) for _ in range(0, 10)]
    print("before sort: {}".format(my_list))
    BinaryInsertion(my_list).sort()
    print("after sort: {}".format(my_list))
