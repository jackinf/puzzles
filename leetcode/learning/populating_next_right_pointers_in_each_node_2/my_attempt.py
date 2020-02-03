from leetcode.learning.populating_next_right_pointers_in_each_node.node import Node


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        curr_node = root
        while curr_node:
            head = curr_node
            while head:
                # attempt to make a connection #1
                if head.left and head.right:
                    head.left.next = head.right

                # attempt to make a connection #2
                head_child = head.right if head.right else head.left
                while head and head_child:
                    if head.next.left:
                        head_child.next = head.next.left
                        break
                    elif head.next.right:
                        head_child.next = head.next.right
                        break
                    if not head.head.next:
                        break
                    head = head.next
                head = head.next

            # find non-null next child node
            head = curr_node
            while head:
                if curr_node.left:
                    curr_node = curr_node.left
                    break
                if curr_node.right:
                    curr_node = curr_node.right
                    break
                head = head.next

            if head is None:
                curr_node = None

        return root


if __name__ == "__main__":
    s = Solution()

    n7 = Node(7)
    # n6 = Node(6)
    n5 = Node(5)
    n4 = Node(4)
    n3 = Node(3, None, n7)
    n2 = Node(2, n4, n5)
    n1 = Node(1, n2, n3)

    # [0,2,4,1,null,3,-1,5,1,null,6,null,8]

    s.connect(n1)

    def show(n: Node):
        if not n:
            return
        print(f'Node {n} -> {n.next}')
        show(n.left)
        show(n.right)
    show(n1)
