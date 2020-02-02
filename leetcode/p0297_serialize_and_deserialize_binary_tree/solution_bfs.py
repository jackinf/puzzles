import collections
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
        if not root:
            return ''
        queue = collections.deque()
        queue.append(root)
        res = ''
        while queue:
            node = queue.popleft()
            if not node:
                res += 'None,'
                continue
            res += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
        return res

    def deserialize(self, data):
        if not data:
            return None
        ls = data.split(',')
        root = TreeNode(int(ls[0]))
        queue = collections.deque()
        queue.append(root)
        i = 1
        while queue and i < len(ls):
            node = queue.popleft()
            if ls[i] != 'None':
                left = TreeNode(int(ls[i]))
                node.left = left
                queue.append(left)
            i += 1
            if ls[i] != 'None':
                right = TreeNode(int(ls[i]))
                node.right = right
                queue.append(right)
            i += 1
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

    # dfs left traversal
    def dfs_preorder_traversal(node):
        s = [node]
        res = []
        while s:
            curr = s.pop()
            res.append(curr.val)
            if curr.right:
                s.append(curr.right)
            if curr.left:
                s.append(curr.left)

        print(res)

    def dfs_inorder_traversal(node):
        s = []
        curr = node
        res = []
        while curr or s:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            res.append(curr.val)
            curr = curr.right

        print(res)

    def dfs_postorder_traversal(node):
        s = [node]
        res = []
        while s:
            curr = s.pop()
            res.append(curr.val)

            if curr.left:
                s.append(curr.left)
            if curr.right:
                s.append(curr.right)

        print(res[::-1])

    print('DFS pre-order traversal')
    dfs_preorder_traversal(deserialized)

    print('DFS in-order traversal')
    dfs_inorder_traversal(deserialized)

    print('DFS post-order traversal')
    dfs_postorder_traversal(deserialized)
