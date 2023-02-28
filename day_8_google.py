'''
A unival tree (which stands for "universal value")
is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 '''

from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(val: int, depth: int) -> Optional[Node]:
    MAX_DEPTH = 4
    node = None

    if depth < MAX_DEPTH:
        node = Node(val)
        depth = depth + 1
        node.left = build_tree(0, depth=depth)
        node.right = build_tree(1, depth=depth)
    return node


def serialize(node):
    print(node.val)
    if (node.left is not None):
        serialize(node.left)
    if (node.right is not None):
        serialize(node.right)


tree = build_tree(1, 0)
print(serialize(tree))
