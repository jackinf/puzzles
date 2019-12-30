from pprint import pprint
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        length = 0
        while current is not None:
            length += 1
            current = current.next

        current = head
        index = 0
        previous = None
        while current is not None:
            if index == length - n:
                if previous is None:
                    head = current.next
                else:
                    previous.next = current.next
            index += 1
            previous = current
            current = current.next

        return head


def fromArrayToListNode(arr: List[int]) -> ListNode:
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head


def fromListNodeToArray(head: ListNode) -> List[int]:
    current = head
    list = []
    while current is not None:
        list.append(current.val)
        current = current.next
    return list


sol = Solution()
pprint(fromListNodeToArray(sol.removeNthFromEnd(fromArrayToListNode([1, 2, 3, 4, 5]), 2)))
pprint(fromListNodeToArray(sol.removeNthFromEnd(fromArrayToListNode([1]), 1)))
pprint(fromListNodeToArray(sol.removeNthFromEnd(fromArrayToListNode([1]), 0)))
pprint(fromListNodeToArray(sol.removeNthFromEnd(fromArrayToListNode([1]), 2)))
pprint(fromListNodeToArray(sol.removeNthFromEnd(fromArrayToListNode([1, 2, 3]), 3)))