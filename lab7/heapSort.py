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

    
def selection_sort(lst: List[int]) -> None:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):  
            if lst[j] < lst[min_idx]:     
                min_idx = j
        if i != min_idx:
            lst[i], lst[min_idx] = lst[min_idx], lst[i]


def selection_sort_shift(lst:List) -> None:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j

        if i != min_idx:
            x = lst.pop(min_idx)
            lst.insert(i,x)


if __name__ == "__main__":
    data = [Element(key, value) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    que = Heap(data)
    que.sort()
    que.print_tab()
    que.print_tree(0,0)

    tab = []
    for i in range(10000):
        tab.append(randrange(100))

    #test 2
    que_2 = Heap(tab)
    t_start = time.perf_counter()
    que_2.sort()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start)) 

    help_list_1 = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    help_list_2 = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]

    selection_sort(help_list_1)

    print(f'Zadana tablica dla sortowania selection ze swapem:\n{help_list_1}')
    print('Algorytym selection ze swapem nie jest stabilny')

    random_list = []
    for i in range(10000):
        random_list.append(randrange(100))
    random_list_2 = deepcopy(random_list)
    random_list_3 = deepcopy(random_list)
    

    start = time.time()
    selection_sort(random_list_2)
    stop = time.time()
    print(f'Czas sortowania 10000 liczb dla algorytmu selection sort z swapem to: {stop - start}\n\n')

    selection_sort_shift(help_list_2)
    print(f'Zadana tablica dla sortowania selection ze shiftem:\n{help_list_2}')
    print('Algorytym selection ze shiftem jest stabilny')

    start = time.time()
    selection_sort_shift(random_list_3)

    stop = time.time()
    print(f'Czas sortowania 10000 liczb dla algorytmu selection sort z shiftem to: {stop - start}')
    
