# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(curr, prev):
            if not curr:
                return prev
            ne = curr.next
            curr.next = prev
            return reverse(ne, curr)

        n1 = reverse(l1, None)
        n2 = reverse(l2, None)

        carry = 0
        reshead = ListNode(-1, None)
        prevres = reshead

        while n1 or n2:
            subres = 0
            if n1:
                subres += n1.val
                n1 = n1.next
            if n2:
                subres += n2.val
                n2 = n2.next
            if carry == 1:
                subres += 1
            carry = 1 if subres >= 10 else 0
            subres %= 10
            prevres.next = ListNode(subres, None)
            prevres = prevres.next

        if carry == 1:
            prevres.next = ListNode(1, None)

        return reverse(reshead.next, None)

