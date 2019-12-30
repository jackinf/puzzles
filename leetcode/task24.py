from typing import Tuple, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(a: ListNode, b: ListNode) -> Tuple[ListNode, ListNode]:
            (a.next, b.next) = (b.next, a)
            return a, b

        if head is None:
            return None

        current = head
        prev = None
        while current is not None and current.next is not None:
            (newCurr, newCurrNext) = swap(current, current.next)

            if prev is None:  # is it first swap
                head = newCurrNext
            else:
                prev.next = newCurrNext

            prev = newCurr
            current = newCurr.next

        return head


def fromA(arr: List[int]) -> ListNode:
    if arr is None or len(arr) == 0:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head


def toList(head: ListNode) -> List[int]:
    if head is None:
        return None
    current = head
    list = []
    while current is not None:
        list.append(current.val)
        current = current.next
    return list


sol = Solution()
print(toList(sol.swapPairs(fromA([1, 2, 3, 4]))))
print(toList(sol.swapPairs(fromA([1, 2, 3, 4, 5, 6, 7, 8, 9]))))
print(toList(sol.swapPairs(fromA([]))))
print(toList(sol.swapPairs(fromA([1]))))
