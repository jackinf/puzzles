from leetcode.p0234_palindrome_linked_list.list_node import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        current_head = head
        current_tail = ListNode(head.val)
        while current_head.next:
            current_tail, current_tail.next = ListNode(current_head.next.val), current_tail
            current_head = current_head.next

        current_head = head
        while current_tail:
            print('current_tail', current_tail.val, 'current_head', current_head.val)
            if current_tail.val != current_head.val:
                return False
            current_tail = current_tail.next
            current_head = current_head.next

        return True


if __name__ == "__main__":
    s = Solution()

    arr = [1, 2, 3, 2, 1]
    head = ListNode(arr[0])
    current = head
    for item in arr[1:]:
        current.next = ListNode(item)
        current = current.next

    print(s.isPalindrome(None))