import random

def randomLevel(p, maxLevel):
    lvl = 1   
    while random.random() < p and lvl < maxLevel:
        lvl += 1
    return lvl

class Element:
    def __init__(self, key, value, max_level, levels=0):
        self.key = key
        self.value = value
        self.max_level = max_level
        self.levels = levels
        self.next = [None for _ in range(self.levels)]

    @property
    def levels(self):
        return self.__levels

    @levels.setter
    def levels(self, levels):
        if levels == 0:
            probability = 0.5
            levels_count = 1
            while random.random() < probability and levels_count < self.max_level:
                levels_count += 1
            self.__levels = levels_count
        else:
            self.__levels = levels

    def __str__(self):
        return f"({self.key}:{self.value})"


class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.head = Element("HEAD", "HEAD", max_level, max_level)

    def search(self, key):
        current = self.head
        for level in range(self.max_level - 1, -1, -1):
            while current.next[level] and current.next[level].key < key:
                current = current.next[level]

        current = current.next[0]
        if current is None or current.key != key:
            return None

        return current.value

    def insert(self, key, value):
        if self.search(key) is not None:
            self.remove(key)
        previous = [self.head for _ in range(self.max_level)]
        current = self.head

        for level in range(self.max_level - 1, -1, -1):
            while current.next[level] and current.next[level].key < key:
                current = current.next[level]
            previous[level] = current

        new_levels = randomLevel(0.5, self.max_level)
        new_element = Element(key, value, self.max_level, new_levels)

        for level in range(new_levels):
            new_element.next[level] = previous[level].next[level]
            previous[level].next[level] = new_element

    def remove(self, key):
        previous = [self.head for _ in range(self.max_level)]
        current = self.head

        for level in range(self.max_level - 1, -1, -1):
            while current.next[level] and current.next[level].key < key:
                current = current.next[level]
            previous[level] = current

        current = current.next[0]

        if current is not None and current.key == key:
            for level in range(self.max_level):
                if previous[level].next[level] != current:
                    break
                previous[level].next[level] = current.next[level]

    def __str__(self):
        string_repr = ""
        current = self.head.next[0]
        while current:
            string_repr += str(current) + " -> "
            current = current.next[0]
        return string_repr + "END"

    def displayList_(self):
        node = self.head.next[0]
        keys = []
        while node is not None:
            keys.append(node.key)
            node = node.next[0]

        for level in range(self.max_level - 1, -1, -1):
            print(f"Level {level}: ", end="")
            node = self.head.next[level]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print("      ", end="")
                    idx += 1
                print(f"({node.key}:{node.value})", end=" ")
                idx += 1
                node = node.next[level]
            print()

if __name__ == "__main__":
    random.seed(42)
    skip_list = SkipList(6)
    data = list(zip(range(1, 16), "ABCDEFGHIJKLMNO"))


    for key, value in data:
        skip_list.insert(key, value)

   
    skip_list.displayList_()
    print(skip_list.search(2))
    skip_list.insert(2, "Z")
    print(skip_list.search(2))
    skip_list.remove(5)
    skip_list.remove(6)
    skip_list.remove(7)
    skip_list.displayList_()
    skip_list.insert(6, "W")
 
    skip_list.displayList_()
    print()

    data.reverse()
    skip_list = SkipList(6)
    for key, value in data:
        skip_list.insert(key, value)


    skip_list.displayList_()
    print(skip_list.search(2))
    skip_list.insert(2, "Z")
    print(skip_list.search(2))
    skip_list.remove(5)
    skip_list.remove(6)
    skip_list.remove(7)
    skip_list.displayList_()
    skip_list.insert(6, "W")
    skip_list.displayList_()
