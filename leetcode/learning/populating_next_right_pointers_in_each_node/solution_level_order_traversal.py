import collections

from leetcode.learning.populating_next_right_pointers_in_each_node.node import Node


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        # Initialize a queue data structure which contains just the root of the tree
        Q = collections.deque([root])

        # Outer while loop which iterates over each level
        while Q:
            size = len(Q)   # Note the size of the queue

            # Iterate over all the nodes on the current level
            for i in range(size):
                node = Q.popleft()  # Pop a node from the front of the queue

                # This check is important. We don't want to establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any point in time. This check ensures we only
                # don't establish next pointers beyond the end of a level
                if i < size - 1:
                    node.next = Q[0]

                # Add the children, if any, to the back of the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        # Since the tree has now been modified, return the root node
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