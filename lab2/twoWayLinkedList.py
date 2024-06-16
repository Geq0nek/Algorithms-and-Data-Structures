#skonczone

class Element:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkdeList:
    def __init__(self, head=None):
        self.head = head
        self.tail = None

    def destroy(self):
        current = self.head
        while current:
            next_node = current.next
            del current
            current = next_node
        self.head = None
        self.tail = None

    def add(self, data):
        new_elem = Element(data)
        if self.head is None:
            self.head = new_elem
            self.tail = new_elem
            return
        else:
            new_elem.next = self.head
            self.head.prev = new_elem
            self.head = new_elem

    def append(self, data):
        new_elem = Element(data)
        if self.head is None:
            self.head = new_elem
            self.tail = new_elem
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_elem
        new_elem.prev = current
        self.tail = new_elem

    def remove(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None
        

    def remove_end(self):
        if self.is_empty():
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        current = self.head
        while current.next != self.tail:
            current = current.next
        current.next = None
        self.tail = current

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def length(self):
        count = 0

        if self.head is None:
            return count
        
        current = self.head
        while(current):
            current = current.next
            count += 1

        return count
    
    def get(self):
        return self.head.data

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += f"-> {current.data}\n"
            current = current.next

        return result


if __name__ == "__main__":

    example = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)]

    uczelnie = LinkdeList()
    
    
    uczelnie.append(example[0])
    uczelnie.append(example[1])
    uczelnie.append(example[2])
    uczelnie.add(example[3])
    uczelnie.add(example[4])
    uczelnie.add(example[5])

    print(uczelnie)
    print(uczelnie.length())

    uczelnie.remove()
    print(uczelnie.get())
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.append(example[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())



        
        

        










        