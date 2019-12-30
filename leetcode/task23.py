from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            current1 = l1
            current2 = l2
            head = None
            combined = None

            while True:
                if current1 is not None and current2 is not None:
                    chosen = current1 if current2.val > current1.val else current2

                    if combined is None:
                        head = chosen
                        combined = chosen
                    else:
                        combined.next = chosen
                        combined = combined.next

                    # go to the next item
                    if current2.val > current1.val:
                        current1 = current1.next
                    else:
                        current2 = current2.next

                elif current1 is not None and current2 is None:
                    if combined is None:
                        head = combined = current1
                    else:
                        combined.next = current1
                        combined = combined.next

                    current1 = current1.next

                elif current1 is None and current2 is not None:
                    if combined is None:
                        head = combined = current2
                    else:
                        combined.next = current2
                        combined = combined.next

                    current2 = current2.next

                else:  # both are None, end the cycle
                    break

            return head

        if len(lists) == 0:
            return None

        def divide(arr):
            if len(arr) == 2:
                return mergeTwoLists(arr[0], arr[1])
            if len(arr) == 1:
                return arr[0]

            m = len(arr) / 2
            res1 = divide(arr[0:int(m)])
            res2 = divide(arr[int(m):len(arr)])
            return mergeTwoLists(res1, res2)

        master = divide(lists)
        return master


def fromA(arr: List[int]) -> ListNode:
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

input = [ListNode(7), ListNode(49), ListNode(73), ListNode(58), ListNode(30), ListNode(72)]
print(toList(sol.mergeKLists(input)))