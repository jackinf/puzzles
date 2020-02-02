import collections

from leetcode.learning.populating_next_right_pointers_in_each_node.node import Node


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root


if __name__ == "__main__":
    s = Solution()

    n7 = Node(7)
    n6 = Node(6)
    n5 = Node(5)
    n4 = Node(4)
    n3 = Node(3, n6, n7)
    n2 = Node(2, n4, n5)
    n1 = Node(1, n2, n3)

    s.connect(n1)

    def show(n: Node):
        if not n:
            return
        print(f'Node {n} -> {n.next}')
        show(n.left)
        show(n.right)
    show(n1)