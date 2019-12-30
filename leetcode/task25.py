from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


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


class Solution:
    def swapPairs(self, head: ListNode, k: int) -> ListNode:
        current = head
        prev = None
        pre_count = 0
        count = 0

        temp = current
        while temp is not None and pre_count < k:
            temp = temp.next
            pre_count += 1
        if pre_count != k:
            return current

        # Reverse first k nodes of the linked list
        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current. And make rest of the list as
        # next of first node
        if pre_count == k and current is not None:
            head.next = self.swapPairs(current, k)

        return prev


sol = Solution()
print(toList(sol.swapPairs(fromA([1, 2]), 2)))
print(toList(sol.swapPairs(fromA([1, 2, 3, 4, 5]), 6)))
print(toList(sol.swapPairs(fromA([1, 2, 3, 4, 5]), 1)))
print(toList(sol.swapPairs(fromA([1, 2, 3, 4, 5]), 2)))
print(toList(sol.swapPairs(fromA([1, 2, 3, 4, 5, 6, 7, 8]), 3)))
