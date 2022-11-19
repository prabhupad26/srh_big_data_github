from time import time
import random


class BSTNode:
    def __init__(self, root_node):
        self.root_node = root_node
        self.right_sub_node = None
        self.left_sub_node = None

    def insert_node(self, num):
        if num > self.root_node:
            if self.right_sub_node is None:
                self.right_sub_node = BSTNode(num)
            else:
                self.right_sub_node.insert_node(num)
        else:
            if self.left_sub_node is None:
                self.left_sub_node = BSTNode(num)
            else:
                self.left_sub_node.insert_node(num)
            
    def print_tree(self):
        if self.left_sub_node is not None:
            self.left_sub_node.print_tree()
        print(self.root_node)
        if self.right_sub_node is not None:
            self.right_sub_node.print_tree()

    def search_node(self, num):
        if num > self.root_node:
            if self.right_sub_node is not None:
                self.right_sub_node.search_node(num)
            else:
                print(f"{num} is not found in this tree")
        elif num == self.root_node:
            print(f"Match found {self.root_node}")
        else:
            if self.left_sub_node is not None:
                self.left_sub_node.search_node(num)
            else:
                print(f"{num} is not found in this tree")


values = [random.randint(1, 100000) for i in range(10)]
search_value = 1

start_bst = time()
tree = BSTNode(random.randint(1, 10000))
for value in values:
    tree.insert_node(value)
tree.insert_node(311333)
end_bst = time() - start_bst
start_sorted = time()
sorted(values)
end_sorted = time() - start_sorted


# tree.search_node(search_value)
start_print = time()
tree.print_tree()
end_print = time() - start_print
print(f"time taken by bst {end_bst}")
print(f"time taken by sorted {end_sorted}")
print(f"time taken by print {end_print + end_bst}")
