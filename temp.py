class Node:
    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next


class Solution:
    def construct(self, nums):
        head = Node(0)
        curr = head
        for num in nums:
            curr.next = Node(num)
            curr = curr.next
        return head.next

    def print(self, head: Node):
        curr = head
        while curr:
            print(curr.val, end="-")
            curr = curr.next
        print()

    def sort(self, head: Node):
        if not head.next:
            return head

        m = self.split(head)

        head = self.sort(head)
        m = self.sort(m)

        reshead = Node(float('-inf'))
        res = reshead
        curr = head
        while curr and m:
            if curr.val < m.val:
                res.next = curr
                curr = curr.next
            else:
                res.next = m
                m = m.next
            res = res.next

        while curr:
            res.next = curr
            curr = curr.next
            res = res.next

        while m:
            res.next = m
            m = m.next
            res = res.next

        return reshead.next

    def split(self, head: Node):
        prev, slow, fast = head, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return slow


if __name__ == "__main__":
    solution = Solution()
    head = solution.construct([4, 2, 1, 5, 1, 2, 8, 3, 4, 12, 3])
    # solution.print(head)
    head = solution.sort(head)
    solution.print(head)
    # solution.print(head)