from leetcode.p0206_reverse_linked_list.list_node import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse_list_recursively(head)

    def reverse_list_recursively(self, head: ListNode) -> ListNode:
        # base case: find the last element.
        if not head or not head.next:
            return head

        # For found base case, rseturn statement will be executed in order of head's index of N, N-1, N-2, ..., 2, 1
        tail = self.reverse_list_recursively(head.next)
        head.next.next = head
        head.next = None
        return tail

    def reverse_list_iteratively(self, head: ListNode):
        previous = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = previous
            previous = curr
            curr = next_node
        return previous


if __name__ == "__main__":
    s = Solution()

    # Arrange
    arr = [1, 2, 3, 4, 5]
    head = ListNode(arr[0])
    curr = head
    for item in arr[1:]:
        curr.next = ListNode(item)
        curr = curr.next

    # Act
    reversed = s.reverseList(head)

    # Assert
    curr = reversed
    while curr:
        print(curr.val)
        curr = curr.next