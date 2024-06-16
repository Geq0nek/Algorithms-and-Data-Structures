class Root:
    def __init__(self):
        self.root = None

    def insert(self, node):
        self.root = insert(self.root, node)

    def search(self, key):
        temp = self.root
        return search(temp, key)
    
    def delete(self, key):
        self.root = delete_node(self.root, key)

    def height(self):
        return height(self.root)
    
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.data)
     
            self.__print_tree(node.left, lvl+5)

    def print(self):
            lst = []
            def collect_all(root):
                if root is None:
                    return None

                collect_all(root.left)
                lst.append(root)
                collect_all(root.right)


            collect_all(self.root)
            lst.sort(key = lambda x : x.key)
            for i in lst:
                print(f'{i.key} {i.data}', end=', ')
    
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.key} : {self.data}'

    def __repr__(self):
        return self.__str__()
    

def insert(root, node):
    if root is not None:
        if root.key > node.key:
            root.left = insert(root.left, node)

        elif root.key < node.key:
            root.right = insert(root.right, node)

        else:
            root.data = node.data
            return root
    else:
        return node
    
    return root

def search(root, key):
    if root.key > key:
        root = search(root.left, key)
    elif root.key < key:
        root = search(root.right, key)
    else:
        return root.data
    
    return root

def delete_node(root, key):
    if root.key > key:
        root.left = delete_node(root.left, key)
    elif root.key < key:
        root.right = delete_node(root.right, key)
    else:
        if root.right is None:
            help_node = root.left
            root = None
            return help_node
        
        elif root.left is None:
            help_node = root.right
            root = None
            return help_node
        else:
            help_node = root
            help_node = help_node.right
            while help_node.left is not None:
                help_node = help_node.left

            root.data = help_node.data
            root.key = help_node.key
            root.right = delete_node(root.right, help_node.key)
    
    return root

def height(root):
    if root is None:
        return -1
    
    left_height = height(root.left)
    right_height = height(root.right)

    if right_height > left_height:
        return right_height + 1
    else:
        return left_height + 1

if __name__ == '__main__':
    a = Root()
    a.insert(Node(50,'A'))
    a.insert(Node(15,'B'))
    a.insert(Node(62,'C'))
    a.insert(Node(5,'D'))
    a.insert(Node(20,'E'))
    a.insert(Node(58,'F'))
    a.insert(Node(91,'G'))
    a.insert(Node(3,'H'))
    a.insert(Node(8,'I'))
    a.insert(Node(37,'J'))
    a.insert(Node(60,'K'))
    a.insert(Node(24,'L'))
    a.print_tree()
    print(a.print())
    print(a.search(24))
    a.insert(Node(20,'AA'))
    a.insert(Node(6,"M"))
    a.delete(62)
    a.insert(Node(59,"N"))
    a.insert(Node(100,'P'))
    a.delete(8)
    a.delete(15)
    a.insert(Node(55,"R"))
    a.delete(50)
    a.delete(5)
    a.delete(24)
    print(a.height())
    print(a.print())
    a.print_tree()


    