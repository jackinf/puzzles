# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        indexes = {val:idx for idx,val in enumerate(inorder)}
        def helper(l: int, r:int, hashmap):
            if l > r:
                return None
            val = preorder.pop(0)
            index = hashmap[val]
            node = TreeNode(val)
            node.left = helper(l, index-1, hashmap)
            node.right = helper(index+1, r, hashmap)
            return node
        root = helper(0, len(inorder)-1, indexes)
        return root