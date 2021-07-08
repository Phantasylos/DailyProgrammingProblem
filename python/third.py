import ast


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def desirialize(tree_str: str) -> Node:
    if ast.literal_eval(tree_str) is not None:
        for key, value in dict(ast.literal_eval(tree_str)).items():
            if key is not None:
                return Node(key, desirialize(value[0]), desirialize(value[1]))


def serialize(target_node: Node) -> str:
    if target_node is not None:
        return str({f'{target_node.val}': [f'{serialize(target_node.left)}', f'{serialize(target_node.right)}']})


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert desirialize(serialize(node)).left.left.val == 'left.left'
