class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def countlen(curr):
            length = 0
            while curr:
                length += 1
                curr = curr.next
            return length

        l1len, l2len = countlen(l1), countlen(l2)

        head = ListNode(None, None)
        res = head
        if l1len < l2len:
            l1len, l2len = l2len, l1len
            l1, l2 = l2, l1

        for i in range(l1len - l2len):
            res.next = ListNode(l1.val)
            res = res.next
            l1 = l1.next

        for i in range(l2len):
            res.next = ListNode(l1.val + l2.val)
            res = res.next
            l1 = l1.next
            l2 = l2.next

        # resolve carry's
        curr = head.next
        if curr and curr.val >= 10:
            head.next = ListNode(1, curr)
            curr.val -= 10

        while curr and curr.next:
            if curr.next.val >= 10:
                curr.val += 1
                curr.next.val -= 10
            curr = curr.next

        return head.next