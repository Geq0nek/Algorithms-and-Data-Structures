# skonczone


import random
import time


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
    def __init__(self, to_sort = None) -> None:
        self.tab = []
        self.heap_size = 0
        if to_sort:
            for elem in to_sort:
                self.enqueue(elem)
        

    def size(self):
        return len(self.tab)

    def is_empty(self):
        return self.heap_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[0]

    def dequeue(self):
        if self.is_empty():
            return None
        pick = self.peek()
        self.tab[0] = self.tab[self.heap_size - 1]
        self.tab[self.heap_size - 1] = pick
        self.heap_size -= 1
        self.repair()
        return pick

    def repair(self, index=0):
        left = self.left(index)
        right = self.right(index)
        max = index

        if left < self.heap_size and self.tab[max] < self.tab[left]:
            max = left

        if right < self.heap_size and self.tab[max] < self.tab[right]:
            max = right

        if max != index:
            self.tab[index], self.tab[max] = self.tab[max], self.tab[index]
            self.repair(max)

    def enqueue(self, elem):
        if self.heap_size < self.size():
            self.tab[self.heap_size] = elem
        else:
            self.tab.append(elem)
        self.heap_size += 1
        self.repair_enq(self.heap_size - 1)

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
        print("{", end=" ")
        print(*self.tab[: self.heap_size], sep=", ", end=" ")
        print("}")

    def print_tree(self, idx, lvl):
        if idx < self.size():
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * "  ", self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)
            
    def sort(self):
        size = self.heap_size
        for i in range(len(self.tab) - 1, -1, -1):
            self.tab[i] = self.dequeue()
        self.heap_size = size
        
        return self.tab


data = [Element(key, value) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
que = Heap(data)
print(que.sort())
que.print_tab()
que.print_tree(0,0)

# que.print_tab()
# rnd = [random.randint(0, 99) for _ in range(10000)]
# que = Heap(rnd)
# t_start = time.perf_counter()
# que.sort()
# t_stop = time.perf_counter()
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))