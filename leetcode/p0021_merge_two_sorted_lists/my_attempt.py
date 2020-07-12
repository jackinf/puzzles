# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(None)
        result_tail = result
        while l1 and l2:
            if l1.val > l2.val:
                result_tail.next = l2
                l2 = l2.next
            else:
                result_tail.next = l1
                l1 = l1.next
            result_tail = result_tail.next
        if l1:
            result_tail.next = l1
        if l2:
            result_tail.next = l2
        return result.next