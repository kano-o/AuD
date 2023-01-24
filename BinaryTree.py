# Creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


    def insert(self, data):
        if data < self.data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return
        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return

    def print_tree(self):
        if self.left_child:
            self.left_child.print_tree()
        print(self.data),
        if self.right_child:
            self.right_child.print_tree()

    def search(self, val):
        if val == self.data:
            return str(self.data) + ' is found in the BST'
        elif val > self.data:
            if self.right_child:
                return self.right_child.search(val)
            else:
                return str(val) + ' is not part of the BST'
        elif val < self.data:
            if self.left_child:
                return self.left_child.search(val)
            else:
                return str(val) + ' is not part of the BST'
            


# Creating a root node
root = Node(27)

root.insert(14)
root.insert(46)
root.insert(19)
root.insert(15)
root.insert(10)
root.insert(30)

print(root.search(30))
print(root.search(31))
root.print_tree()