# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Accepted, but very slow
    """
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr, curr = [], head
        while curr:
            arr.append(curr)
            curr = curr.next

        if not arr:
            return

        step, curr = 1, arr.pop(0)
        while arr:
            if step % 2 == 1:
                right = arr.pop()
                curr.next = right
                right.next = None
                curr = right
            else:
                left = arr.pop(0)
                curr.next = left
                left.next = None
                curr = left
            step += 1
