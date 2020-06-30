# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1len, l2len = self.getLen(l1), self.getLen(l2)
        l1 = self.addLeadingZeros(l2len - l1len, l1)
        l2 = self.addLeadingZeros(l1len - l2len, l2)
        c, ans = self.combineLists(l1, l2)
        if c > 0:
            new = ListNode(1)
            new.next = ans
            ans = new
        return ans

    def getLen(self, curr):
        l = 0
        while curr:
            l += 1
            curr = curr.next
        return l

    def addLeadingZeros(self, n, curr):
        for i in range(n):
            new = ListNode(0)
            new.next = curr
            curr = new
        return curr

    def combineLists(self, l1, l2):
        if not l1 and not l2:
            return (0, None)
        c, new = self.combineLists(l1.next, l2.next)
        res = l1.val + l2.val + c
        ans = ListNode(res % 10)
        ans.next = new
        return (res // 10, ans)