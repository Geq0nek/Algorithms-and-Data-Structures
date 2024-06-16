import time
from typing import List
from random import *
from copy import deepcopy


class Element:
    def __init__(self, priority, data) -> None:
        self.__data = data
        self.__priority = priority

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority

    def __repr__(self) -> str:
        return f"{self.__priority}: {self.__data}"


class Heap:
    def __init__(self, elemnets_to_sort = None):
        self.tab = []
        self.tab_size = 0
        if elemnets_to_sort:
            for elem in elemnets_to_sort:
                self.enqueue(elem)

    def size(self):
        return len(self.tab)

    def is_empty(self):
        return self.tab_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[0]

    def dequeue(self):
        if self.is_empty():
            return None
        pick = self.peek()
        self.tab[0] = self.tab[self.tab_size - 1]
        self.tab[self.tab_size - 1] = pick
        self.tab_size -= 1
        self.repair()
        return pick

    def repair(self, index=0):
        left = self.left(index)
        right = self.right(index)
        max = index

        if left < self.tab_size and self.tab[max] < self.tab[left]:
            max = left

        if right < self.tab_size and self.tab[max] < self.tab[right]:
            max = right

        if max != index:
            self.tab[index], self.tab[max] = self.tab[max], self.tab[index]
            self.repair(max)

    def enqueue(self, elem):
        if self.tab_size < self.size():
            self.tab[self.tab_size] = elem
        else:
            self.tab.append(elem)
        self.tab_size += 1
        self.repair_enq(self.tab_size - 1)

    def repair_enq(self, index):
        while index > 0 and self.tab[self.parent(index)] < self.tab[index]:
            self.tab[index], self.tab[self.parent(index)] = (
                self.tab[self.parent(index)],
                self.tab[index],
            )
            index = self.parent(index)

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def parent(self, index):
        return (index - 1) // 2

    def print_tab(self):
        element_strings = [f"{element._Element__priority}: {element._Element__data}" for element in self.tab[:self.tab_size]]
        print("{ " + ", ".join(element_strings) + " }")

    def print_tree(self, index, level):
        if index < self.tab_size:
            self.print_tree(self.right(index), level + 1)
            element = self.tab[index]
            if element:
                print("    " * level + repr(element))
            else:
                print(None)
            self.print_tree(self.left(index), level + 1)
            
    def sort(self):
        size = self.tab_size
        for i in range(len(self.tab) - 1, -1, -1):
            self.tab[i] = self.dequeue()
        self.tab_size = size
        
        return self.tab

    
def h_value(list):
    h = 1
    while h < len(list) / 3:
        h = h * 3 + 1
    return h


def shell(list):
    h = h_value(list)
    while h > 0:
        for i in range(h, len(list)):
            temp = list[i]
            j = i
            while j >= h and list[j - h] > temp:
                list[j] = list[j - h]
                j -= h

            list[j] = temp
        h //= 3

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]

        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key


if __name__ == "__main__":
    tab = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    help_list_1 = deepcopy(tab)
    help_list_1 = deepcopy(tab) 
    # data = [Element(key, value) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    # que = Heap(data)
    # que.sort()
    # que.print_tab()
    # que.print_tree(0,0)

    random_tab = []
    for i in range(10000):
        random_tab.append(randrange(100))

    random_tab_2 = deepcopy(random_tab)
    random_tab_3 = deepcopy(random_tab)
    random_tab_4 = deepcopy(random_tab)

    
    t_start = time.perf_counter()
    shell(help_list_1)
    t_stop = time.perf_counter()
    print("Czas sortowania shellsort dla podanej tablicy: ", t_stop - t_start)

    t_start2 = time.perf_counter()
    insertion_sort(help_list_1)
    t_stop2 = time.perf_counter()
    print("Czas sortowania insertion dla podanej tablicy: ", t_stop2 - t_start2)

    t_start3 = time.perf_counter()
    shell(random_tab_2)
    t_stop3 = time.perf_counter()
    print("Czas sortowania shellsort dla tablicy randomowej: ", t_stop3 - t_start3)

    t_start4 = time.perf_counter()
    insertion_sort(random_tab_3)
    t_stop4 = time.perf_counter()
    print("Czas sortowania insertion dla tablicy randomowej: ", t_stop4 - t_start4)

    que = Heap(random_tab_4)
    t_start = time.perf_counter()
    que.sort()
    t_stop = time.perf_counter()
    print("Czas obliczeń sortowania kopcowego dla tablicy randomowej:", "{:.7f}".format(t_stop - t_start)) 