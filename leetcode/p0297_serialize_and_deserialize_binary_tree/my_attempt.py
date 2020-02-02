import math
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.val}"


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return "[]"

        def bfs(node: TreeNode, level: int, res):
            if level >= len(res):
                res.append([])

            if not node:
                res[level].append("null")
            else:
                res[level].append(node.val)
                bfs(node.left, level + 1, res)
                bfs(node.right, level + 1, res)

        results = []
        bfs(root, 0, results)

        # bugfix: remove last level if all values are null
        if all([x == "null" for x in results[-1]]):
            results = results[:-1]

        return "[" + ",".join([str(x) for y in results for x in y]) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        # convert str to array
        if not data or data == "[]":
            return None
        arr = data[1:-1].split(',')
        if not arr:
            return None

        # convert array to dictionary of lists, where each key represents a level
        # "[1,2,3,null,null,4,5]" -> [[1], [2,3], [null,null,4,5]]

        res = []
        for i, val in enumerate(arr):
            level = int(math.log2(i + 1))
            if level >= len(res):
                res.append([])
            if val == "null":
                res[level].append(None)
            else:
                res[level].append(TreeNode(int(val)))

        def solve(level: int):
            if level + 1 >= len(res):
                return

            for i, item in enumerate(res[level]):
                level_items = res[level + 1]
                if item is None:
                    continue
                if 2 * i >= len(level_items):
                    continue

                left_node = level_items[2 * i]
                if left_node:
                    item.left = left_node
                    solve(level + 1)

                right_node = res[level + 1][2 * i + 1]
                if right_node:
                    item.right = right_node
                    solve(level + 1)

        solve(0)

        return res[0][0]


if __name__ == "__main__":
    # Your Codec object will be instantiated and called as such:
    codec = Codec()

    root = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)

    root.left = node_2
    root.right = node_3
    node_3.left = node_4
    node_3.right = node_5

    serialized = codec.serialize(root)
    print(f"serialized: \"{serialized}\"")
    deserialized = codec.deserialize(serialized)

    def show(node: TreeNode):
        if not node:
            return
        print(node.val)
        show(node.left)
        show(node.right)

    show(deserialized)
    # print(deserialized)