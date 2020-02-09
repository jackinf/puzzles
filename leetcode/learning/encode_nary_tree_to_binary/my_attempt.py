from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return f'{self.val}'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.val}'


class Codec:

    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        def traverse(n_node: 'Node', append_right: List['Node'], b_node: 'TreeNode'):
            print(f'node: {n_node.val}, append_right: {append_right}')
            if n_node.children:
                next_node = n_node.children[0]
                b_node.left = TreeNode(next_node.val)
                new_append_right = n_node.children[1:] if n_node.children else []
                traverse(next_node, new_append_right, b_node.left)

            if append_right:
                next_node = append_right.pop(0)
                b_node.right = TreeNode(next_node.val)
                traverse(next_node, append_right, b_node.right)

        b_root = TreeNode(root.val)
        traverse(root, [], b_root)
        return b_root

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        def traverse(b_node: TreeNode, n_node: 'Node', parent_n_node: 'Node'):
            if b_node.left:
                next_node = Node(b_node.left.val, [])
                if not n_node.children:
                    n_node.children = []
                n_node.children.append(next_node)
                traverse(b_node.left, next_node, n_node)
            if b_node.right and parent_n_node:
                if not parent_n_node.children:
                    parent_n_node.children = []
                parent_n_node.children.append(Node(b_node.right.val, []))
                traverse(b_node.right, parent_n_node, parent_n_node)

        n_root = Node(data.val, [])
        traverse(data, n_root, None)
        return n_root


if __name__ == "__main__":
    codec = Codec()

    # test case 1
    n6 = Node(6, [])
    n5 = Node(5, [])
    n4 = Node(4, [])
    n3 = Node(3, [n5, n6])
    n2 = Node(2, [])
    root = Node(1, [n3, n2, n4])

    encoded = codec.encode(root)
    def print_encoded(par_val: str, node: TreeNode):
        if not node:
            return
        print(f'{par_val}->{node.val}', end=" ")
        print_encoded(node.val, node.left)
        print_encoded(node.val, node.right)


    print('print_encoded')
    print_encoded('x', encoded)
    decoded = codec.decode(encoded)
    def print_decoded(par_val: str, node: Node):
        if not node:
            return
        print(f'{par_val}->{node.val}', end=" ")
        for item in node.children:
            print_decoded(node.val, item)

    print()
    print('print_decoded')
    print_decoded('x', decoded)
    print()
    print_decoded('x', root)

    print('finito')
