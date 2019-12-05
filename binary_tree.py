#!/usr/bin/python


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is not None:
            current = self.root
            while True:
                if val < current.value:
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                else:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
        else:
            self.root = Node(val)

    def find(self, val):
        if self.root is not None:
            current = self.root
            parent = None
            while True:
                if val == current.value:
                    return current, parent
                if val < current.value:
                    if current.left is not None:
                        parent = current
                        current = current.left
                    else:
                        return None, None
                else:
                    if current.right is not None:
                        parent = current
                        current = current.right
                    else:
                        return None, None

    def min(self):
        if self.root is not None:
            current = self.root
            while True:
                if current.left is not None:
                    current = current.left
                else:
                    return current

    def max(self):
        if self.root is not None:
            current = self.root
            while True:
                if current.right is not None:
                    current = current.right
                else:
                    return current

    def remove(self, val):

        def replace(current):
            if current.left is None and current.right is None:
                return None
            elif current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            else:
                left = current.left
                right = current.right
                current = current.right
                previous = None
                while current.left is not None:
                    previous = current
                    current = current.left
                current.left = left
                if previous:
                    previous.left = None
                if right != current:
                    current.right = right
                else:
                    current.right = None
                return current

        if self.root is not None:
            node, parent = self.find(val)
            if parent is None:
                if node is not None:
                    self.root = replace(node)
                else:
                    self.root = None
            else:
                if parent.left == node:
                    parent.left = replace(node)
                else:
                    parent.right = replace(node)

    def show(self):
        def show_node(current, step):
            print("\t\t" * step, end="")
            print(current.value, end="\t")
            if current.left:
                print(f"L: {current.left}", end="")
            else:
                print(f"L: None", end="")
            if current.right:
                print(f"\tR: {current.right}", end="")
            else:
                print(f"\tR: None", end="")
            print()
            if current.left:
                show_node(current.left, step)
            if current.right:
                show_node(current.right, step + 1)

        if self.root is not None:
            show_node(self.root, 0)
        else:
            print("root: None")

tree = BinaryTree()
# tree.add(6)
# tree.add(3)
# tree.add(7)
# tree.add(4)
# tree.add(1)
# tree.add(8)
# tree.add(6)
#      6
#   3     7
# 1   4 6   8

for i in [3, 6, 9, 8, 5, 2, 1, 4, 7, 0]:
    tree.add(i)
#          3
#      2        6
#    1       5     9
#  0       4     8
#               7

tree.show()
print(f"min: {tree.min()}, max: {tree.max()}")
tree.remove(8)
tree.remove(6)
tree.remove(0)
tree.remove(3)
tree.show()
print(f"min: {tree.min()}, max: {tree.max()}")
