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


values = [1, 3, 5, 4, 6, 66, 8, 56, 5, 4]
search_value = 1

tree = BSTNode(67)
for value in values:
    print(f"Inserting {value}")
    tree.insert_node(value)

tree.search_node(search_value)

tree.print_tree()

