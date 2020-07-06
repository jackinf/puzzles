class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        m = self.split(head)

        head = self.sortList(head)
        m = self.sortList(m)

        dummy = tail = ListNode(float('-inf'))
        curr = head
        while curr and m:
            if curr.val < m.val:
                tail.next = curr
                curr = curr.next
            else:
                tail.next = m
                m = m.next
            tail = tail.next

        while curr:
            tail.next = curr
            curr = curr.next
            tail = tail.next

        while m:
            tail.next = m
            m = m.next
            tail = tail.next

        return dummy.next

    def split(self, head):
        prev, slow, fast = head, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return slow



def construct(nums):
    head = ListNode(0)
    curr = head
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return head.next


def printNode(head: ListNode):
    curr = head
    while curr:
        print(curr.val, end="-")
        curr = curr.next
    print()


if __name__ == "__main__":
    solution = Solution()
    head = construct([4, 2, 1, 5, 1, 2, 8, 3, 4, 12, 3])
    head = solution.sortList(head)
    printNode(head)
