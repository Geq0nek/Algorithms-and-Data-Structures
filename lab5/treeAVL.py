class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class Root:
    def __init__(self):
        self.root = None

    def search(self, key):
        return search(self.root, key)

    def insert(self, key, data):
        self.root = insert(self.root, key, data)

    def delete(self, key):
        self.root = delete(self.root, key)

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __str__(self):
        lst = []

        def collect_all(root):
            if root is None:
                return None

            collect_all(root.left)
            lst.append((root.key, root.data))
            collect_all(root.right)

        collect_all(self.root)
        lst.sort(key=lambda x: x[0]) 
        res = ', '.join(f'{key} {data}' for key, data in lst)  
        return res
    
    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.data)
     
            self.__print_tree(node.left, lvl+5)


def search(node, key):
    if node is None:
        return None

    if node.key == key:
        return node.data

    if key < node.key:
        if node.left:
            return search(node.left, key)
    else:
        if node.right:
            return search(node.right, key)


def insert(node, key, data):
    if node is None:
        return Node(key, data)

    if key < node.key:
        node.left = insert(node.left, key, data)
    elif key > node.key:
        node.right = insert(node.right, key, data)
    else:
        node.data = data
        return node

    node.height = 1 + max(
        get_height(node.left), get_height(node.right)
    )

    balance = get_balance(node)

    return balance_node(node, balance)


def delete(node, key):
    if node is None:
        return None

    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            min_right = min_value_node(node.right)
            node.key = min_right.key
            node.data = min_right.data
            node.right = delete(node.right, min_right.key)

    node.height = 1 + max(
        get_height(node.left), get_height(node.right)
    )

    balance = get_balance(node)
    return balance_node(node, balance)


def lrotate(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node

    node.height = 1 + max(
        get_height(node.left), get_height(node.right)
    )
    new_root.height = 1 + max(
        get_height(new_root.left), get_height(new_root.right)
    )

    return new_root


def rrotate(node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node

    node.height = 1 + max(
        get_height(node.left), get_height(node.right)
    )
    new_root.height = 1 + max(
        get_height(new_root.left), get_height(new_root.right)
    )
    return new_root


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def get_height(node):
    if node is None:
        return 0
    return node.height


def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)


def balance_node(node, balance):
    if balance > 1 and get_balance(node.left) >= 0:
        return rrotate(node)

    if balance < -1 and get_balance(node.right) <= 0:
        return lrotate(node)

    if balance > 1 and get_balance(node.left) < 0:
        node.left = lrotate(node.left)
        return rrotate(node)

    if balance < -1 and get_balance(node.right) > 0:
        node.right = rrotate(node.right)
        return lrotate(node)

    return node

if __name__ == "__main__":
    bst = Root()

    data = {
        50: 'A', 15: 'B', 62: 'C', 5: 'D', 2: 'E', 1: 'F', 11: 'G', 100: 'H', 7: 'I', 
        6: 'J', 55: 'K', 52: 'L', 51: 'M', 57: 'N', 8: 'O', 9: 'P', 10: 'R', 99: 'S', 12: 'T'
    }

    for key, value in data.items():
        bst.insert(key, value)

    bst.print_tree()
    print(bst)
    print(bst.search(10))
    bst.delete(50)
    bst.delete(52)
    bst.delete(11)
    bst.delete(57)
    bst.delete(1)
    bst.delete(12)
    bst.insert(3, "AA")
    bst.insert(4, "BB")
    bst.delete(7)
    bst.delete(8)
    bst.print_tree()
    print(bst)



