

'''
Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(num_nodes):

    left_size = num_nodes / 2
    right_size = num_nodes / 2

    return Node('root')


def deserialize(tree):
    pass


def serialize(node):
    print(node.val)
    if (node.left is not None):
        serialize(node.left)
    if (node.right is not None):
        serialize(node.right)


tree = build_tree(8)
serialize(tree)
