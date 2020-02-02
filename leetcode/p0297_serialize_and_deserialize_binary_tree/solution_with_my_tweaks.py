import math
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.val}"


class Codec:
    def serialize(self, root):
        def dfs(node: TreeNode, res: List[str]):
            if node is None:
                res.append("null")
                return
            else:
                res.append(str(node.val))
                dfs(node.left, res)
                dfs(node.right, res)
        res = []
        dfs(root, res)
        return f"{','.join(res)}"

    def deserialize(self, string):
        def solve(l):
            item = l.pop(0)
            if item == "null":
                return
            node = TreeNode(item)
            node.left = solve(l)
            node.right = solve(l)
            return node

        data = string.split(',')
        root = solve(data)
        return root


if __name__ == "__main__":
    # Your Codec object will be instantiated and called as such:
    codec = Codec()

    root = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)

    # root.left = node_2
    # root.right = node_3
    # node_3.left = node_4
    # node_3.right = node_5

    root.left = node_2
    root.right = node_5
    node_2.left = node_3
    node_2.right = node_4

    serialized = codec.serialize(root)
    print(serialized)
    deserialized = codec.deserialize(serialized)
    print(deserialized)