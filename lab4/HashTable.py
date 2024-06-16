from copy import deepcopy

class InsertError(Exception):
    def __init__(self):
        super().__init__(f'No space in the table! This item cannot be inserted')

class NotFoundError(Exception):
    def __init__(self,key):
        self.key = key
        super().__init__(f'Element with a key {self.key} does not appear in the table')

class Element:
    def __init__(self,key,value):
        self.key = key
        self.value = value

class Hashtable:
    def __init__(self,size,*,c1 = 1,c2 = 0):
        self.size = size
        self.tab = [None for i in range(self.size)]
        self.c1 = c1
        self.c2 = c2

    def hash(self,data):
        sum = 0

        if isinstance(data, str):
            for letter in data:
                sum += ord(letter)
                    
            return sum % self.size

        return data % self.size

    def conflict(self,data):
        help = deepcopy(data)
        empty_slot_flag = any(v is None for v in self.tab)

        if empty_slot_flag:
            i = 1
            while self.tab[data] is not None:
                data = (help + self.c1 * i + self.c2 * i ** 2) % self.size
                i += 1

                if i > 1000 * self.size:
                    raise InsertError
        else:
            raise InsertError

        return data


    def search_conflict(self, index, data):
        help = deepcopy(index)
        i =  0
        while True:
            index = (help + self.c1 * i + self.c2 * i ** 2) % self.size
            i += 1                                                                  
            if self.tab[index] is not None:
                if self.tab[index].key == data:
                    return index

            if i > self.size :
                raise NotFoundError(data)

    def search(self,data):
        index = self.hash(data)

        if self.tab[index] is not None:                            
            if self.tab[index].key == data:
                return self.tab[index].value                        
            else:
                try:
                    index = self.search_conflict(index, data)
                    return self.tab[index].value                        

                except NotFoundError:
                    print('The given element does not exist')

        else:
            try:
                index = self.search_conflict(index,data)
                return self.tab[index].value                                
                                                                            
            except NotFoundError:                                         
                print('The given element does not exist')
        
        return None

    def insert(self,data):
        index = self.hash(data.key)

        if self.tab[index] is not None:
            if self.tab[index].key == data.key:
                self.tab[index].value = data.value
            else:
                try:
                    index = self.conflict(index)
                    self.tab[index] = data
                except InsertError:
                    print('No space in the table')
        else:
            self.tab[index] = data


    def remove(self,data):

        index = self.hash(data)
        
        if self.tab[index] is not None:
            if self.tab[index].key == data:
                self.tab[index] = None
            else:
                try:
                    index = self.search_conflict(index, data)
                    self.tab[index] = None
                except NotFoundError:
                    print('The item does not exist')
        else:
            try:
                index = self.self.search_conflict(index, data)
                self.tab[index] = None
            except NotFoundError:
                print('The item does not exist')


    def __str__(self):
        x = '{'
        x += ', '.join([f'{v.key} : {v.value}' if v is not None else 'None' for v in self.tab])
        x += ' }'
        return x




def test1(c1 = 1, c2 = 0):
    hash = Hashtable(13,c1=c1,c2=c2)
    for i in range(1, 16):
        if i == 6:
            hash.insert(Element(18, chr(64 + i)))
        elif i == 7:
            hash.insert(Element(31, chr(64 + i)))
        else:
            hash.insert(Element(i, chr(64 + i)))
    print(hash)
    print(hash.search(5))
    print(hash.search(14))
    hash.insert(Element(5, "Z"))

    print(hash.search(5))
    hash.remove(5)
    print(hash)
    print(hash.search(31))
    hash.insert(Element('test','W'))




def test2(c1 = 1, c2 = 0):
    hash = Hashtable(13,c1=c1,c2=c2)
    for i in range(1,14):
        hash.insert(Element(i*13,chr(64+i)))



if __name__ == '__main__':
    test1()
    
    test2()
  
    test2(c1=0,c2=1)
    
    test1(c1=0,c2=1)

 