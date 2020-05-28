class Node:
    next: 'Node'
    val: int

    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, node: Node):
        head = node
        seen = set()
        prev = None
        while head:
            if head.val in seen:
                prev.next = head.next
            else:
                seen.add(head.val)
                prev = head
            head = head.next
        return node