from typing import List, Dict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        hashmap = {val:idx for idx,val in enumerate(inorder)}
        return self.solve(hashmap, postorder, 0, len(inorder)-1)

    def solve(self, hashmap: Dict[int, int], postorder: List[int], in_left: int, in_right: int):
        if in_left > in_right:
            return None

        val = postorder.pop()
        index = hashmap[val]

        node = TreeNode(val)
        node.right = self.solve(hashmap, postorder, index + 1, in_right)
        node.left = self.solve(hashmap, postorder, in_left, index - 1)
        return node


if __name__ == "__main__":
    s = Solution()
    postorder = [9, 15, 7, 20, 3]
    inorder = [9, 3, 15, 20, 7]
    node = s.buildTree(inorder, postorder)
    def show(n: TreeNode):
        if not n:
            return
        print(n.val, end=", ")
        show(n.left)
        show(n.right)


    show(node)