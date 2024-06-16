size_of_data = 6

class Node:
    def __init__(self) -> None:
        self.data = [None for _ in range(size_of_data)]
        self.fill = 0  
        self.next = None  


class UnrolledLinkedList:
    def __init__(self) -> None:
        self.head = None  
        self.size = 0  

    def get(self, index) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current = self.head
        while current:
            if index < current.fill:
                return current.data[index]
            index -= current.fill
            current = current.next

    def insert(self, index, value) -> None:
        if index < 0:
            raise IndexError("Index out of range")

        if self.head is None:
            self.head = Node()
            self.head.data[0] = value
            self.head.fill += 1
            self.size += 1
            return

        current = self.head
        previous = None

        while current and index >= current.fill:
            previous = current
            index -= current.fill
            current = current.next

        if current is None:
            previous.next = Node()
            current = previous.next

        if current.fill == len(current.data):
            new_node = Node()
            mid = len(current.data) // 2
            new_node.data[:len(current.data) - mid] = current.data[mid:]
            new_node.fill = len(current.data) - mid
            current.fill = mid

            if index < current.fill:
                current.data.insert(index, value)
                current.fill += 1
            else:
                index -= current.fill
                new_node.data.insert(index, value)
                new_node.fill += 1

                new_node.next = current.next
                current.next = new_node
        else:
            current.data.insert(index, value)
            current.fill += 1

        self.size += 1


    def delete(self, index) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        if index == 0:
            self.head.data.pop(0)
            self.head.fill -= 1
            self.size -= 1
            if self.head.fill == 0:
                self.head = self.head.next if self.head.next else None
            return

        current = self.head
        previous = None

        while current and index >= current.fill:
            previous = current
            index -= current.fill
            current = current.next

        current.data.pop(index)
        current.fill -= 1
        self.size -= 1

        # if current.fill < len(current.data) // 2:
        #     if current.next and current.next.fill > len(current.next.data) // 2:
        #         current.data.append(current.next.data.pop(0))
        #         current.fill += 1
        #         current.next.fill -= 1
        #     elif current.next:
        #         current.data.extend(current.next.data[:current.next.fill])
        #         current.fill += current.next.fill
        #         current.next = current.next.next
        

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.data[:current.fill], end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":

    size_of_array = 6
    linked_list = UnrolledLinkedList()

    for i in range(1, 10):
        linked_list.insert(i-1, i)

    print("Element for id = 4:", linked_list.get(4))

    linked_list.insert(1, 10)
    linked_list.insert(8, 11)

    linked_list.print_list()

    linked_list.delete(1)
    linked_list.delete(2)

    linked_list.print_list()
            