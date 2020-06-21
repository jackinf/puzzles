class Solution:
     def solve(self, node, target):
         closest = node.val
         while node:
             closest = min(node.val, closest, key=lambda x: abs(target-x))
             node = node.left if node.left else node.right
         return closest