# from collections import Generator

from leetcode.p0234_palindrome_linked_list.list_node import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()


if __name__ == "__main__":
    s = Solution()

    arr = [1, 2, 3, 2]
    head = ListNode(arr[0])
    current = head
    for item in arr[1:]:
        current.next = ListNode(item)
        current = current.next

    print(s.isPalindrome(head))