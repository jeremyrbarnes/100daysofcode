

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


from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def multiply_node_name(name: str, num_times: int):
    node_name = ""
    for x in range(0, num_times):
        node_name += name + "."
    return node_name.rstrip(node_name[-1])


def build_tree(node_name: str, depth: int) -> Optional[Node]:
    MAX_DEPTH = 4
    node = None

    if depth < MAX_DEPTH:
        node = Node(node_name)
        depth = depth + 1
        node.left = build_tree(node_name + ".left", depth=depth)
        node.right = build_tree(node_name + ".right", depth=depth)
    return node


def deserialize(tree):
    print(tree)


def serialize(node):
    print(node.val)
    if (node.left is not None):
        serialize(node.left)
    if (node.right is not None):
        serialize(node.right)


tree = build_tree('root', 0)
deserialize(serialize(tree))
