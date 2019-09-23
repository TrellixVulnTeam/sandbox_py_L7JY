class Tree:
    root = None

    def __iter__(self):
        def g(node):
            if node:
                yield node
                yield from g(node.left)
                yield from g(node.right)

        return g(self.root)


class Node:
    left = None
    right = None
    value = None

    def __init__(self, value):
        self.value = value


def populate_tree(node, vals, left):
    if vals:
        node.left = Node(vals[0])
        if len(vals) > 1:
            node.right = Node(vals[1])
        if left:
            populate_tree(node.left, vals[2:], True)
        else:
            populate_tree(node.right, vals[2:], False)


def main():
    tree = Tree()
    tree.root = Node(42)
    NODES = (1, 2, 3, 4, 5, 6)

    populate_tree(tree.root, NODES, True)

    for node in tree:
        print(node.value)


if __name__ == '__main__':
    main()
