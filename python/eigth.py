
class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_uni_trees(node, count=0) -> int:
    if node is None:
        return count

    count = count_uni_trees(node.left, count)
    count = count_uni_trees(node.right, count)

    if (node.right is None and node.left is None) \
            or (node.right is not None and node.left is not None and node.right.val == node.left.val):
        return count + 1

    return count


if __name__ == "__main__":
    first = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0, Node(0))))
    tmp = count_uni_trees(first)
    assert tmp == 5
