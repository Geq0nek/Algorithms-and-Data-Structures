from typing import Union


class CyclicQueue:
    def __init__(self):
        self.array = [None for _ in range(5)]
        self.id_enqueue = 0
        self.id_dequeue = 0
    
    @property
    def size(self) -> int:
        return len(self.array)

    def is_empty(self) -> bool:
        return self.id_dequeue == self.id_enqueue
    
    def peek(self) -> Union[None, int]:
        if self.is_empty():
            return None
        
        return self.array[self.id_dequeue]
    
    def dequeue(self) -> Union[int, None]:
        curr = self.array[self.id_dequeue]

        if not curr:
            return None
        
        self.array[self.id_dequeue] = None

        if self.id_dequeue == self.size - 1:
            self.id_dequeue = 0
        else:
            self.id_dequeue += 1

        return curr

    def enqueue(self, value) -> None:
        self.array[self.id_enqueue] = value

        if self.id_enqueue == self.size - 1:
            self.id_enqueue = 0
        else:
            self.id_enqueue += 1
        if self.id_enqueue == self.id_dequeue:
            new_list = [None for _ in range(self.size * 2)]
            new_list[0:self.id_enqueue] = self.array[0:self.id_enqueue]  
            new_list[-(self.size - self.id_enqueue):] = self.array[self.id_enqueue:]  
            self.id_dequeue += self.size  
            self.array = new_list

    def current_queue(self) -> str:
        elements = []
        curr = self.id_dequeue
        for _ in range(self.size):
            if self.array[curr] is None:
                break
            elements.append(str(self.array[curr]))
            curr = (curr + 1) % self.size
        return "[" + ", ".join(elements) + "]"


    def __str__(self):
        return f"{self.array}"
    

if __name__ == '__main__':

    q = CyclicQueue()
    for i in range(1, 5):
        q.enqueue(i)

    print(q)
    print(q.current_queue())
    print(q.dequeue())
    print(q.peek())
    print(q.current_queue())

    for i in range(5, 9):
        q.enqueue(i)

    print(q)

    elem = q.dequeue()
    while elem is not None:
        print(elem)
        elem = q.dequeue()

    print(q.current_queue())