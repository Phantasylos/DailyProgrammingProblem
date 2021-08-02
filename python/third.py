# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and
# deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


import ast


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(tree_str: str) -> Node:
    if ast.literal_eval(tree_str) is not None:
        for key, value in dict(ast.literal_eval(tree_str)).items():
            if key is not None:
                return Node(key, deserialize(value[0]), deserialize(value[1]))


def serialize(target_node: Node) -> str:
    if target_node is not None:
        return str({f'{target_node.val}': [f'{serialize(target_node.left)}', f'{serialize(target_node.right)}']})


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
