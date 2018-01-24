# -*- coding: utf-8 -*-
import random
import math


class ShellSort(object):
    def __init__(self, original_list):
        self.original_list = original_list

    def sort(self):
        length = len(self.original_list)
        step = int(math.ceil(length / 2))
        while step:
            for index in range(0, step):
                index_list = []
                base = index
                index_list.append(base)
                while True:
                    if base + step > length - 1:
                        break
                    base += step
                    index_list.append(base)
                print(index_list)
                self.straight_sort(index_list)
                print(self.original_list)
            if step == 1:
                step -= 1
            step = int(math.ceil(step / 2))

    def straight_sort(self, index_list):
        temp_sort_list = [self.original_list[index] for index in index_list]
        for i in range(1, len(temp_sort_list)):
            for j in range(0, i):
                if temp_sort_list[i] < temp_sort_list[j]:
                    temp_sort_list[j], temp_sort_list[i] = temp_sort_list[i], temp_sort_list[j]
        for index, i in enumerate(index_list):
            self.original_list.insert(i, temp_sort_list[index])
            del self.original_list[i+1]


if __name__ == '__main__':
    # my_list = [random.randint(0, 100) for _ in range(0, 10)]
    my_list = [29, 87, 23, 33, 38, 99, 4, 99, 94, 25]
    print("before sort: {}".format(my_list))
    ShellSort(my_list).sort()
    print("after sort: {}".format(my_list))
