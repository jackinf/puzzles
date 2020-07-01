# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if n == m:
            return head

        prehead = ListNode(None, head)
        curr = head
        prev = prehead
        x = 1

        while curr:
            if x == m:
                a = prev
                prev = curr
                curr = curr.next

                x += 1
                continue
            elif x == n:
                b = curr.next
                c = a.next

                curr.next = prev
                a.next = curr
                c.next = b
                curr = b

                x += 1
                continue

            if m < x < n:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

                x += 1
            else:
                prev = curr
                curr = curr.next
                x += 1

        return prehead.next