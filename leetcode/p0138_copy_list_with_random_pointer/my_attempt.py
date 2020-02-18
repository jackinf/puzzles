# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        return f'{self.val}'


class Solution:
    """
    Accepted
    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        self.cache = {}
        c_head = self.traverse(head)

        curr = head
        while curr:
            c_curr = self.cache[curr]
            if curr.random:
                c_curr.random = self.cache[curr.random]
            curr = curr.next

        return c_head

    def traverse(self, node: 'Node') -> 'Node':
        cNode = self.copy(node)
        if node.next and not cNode.next:
            cNode.next = self.traverse(node.next)
        return cNode

    def copy(self, node: 'Node'):
        if node in self.cache:
            return self.cache[node]
        cNode = Node(node.val)
        self.cache[node] = cNode
        return cNode


if __name__ == "__main__":
    s = Solution()
    n1 = Node(1)
    n10 = Node(10, n1)
    n11 = Node(11, n10)
    n13 = Node(13, n11)
    n7 = Node(7, n13)

    n7.random = None
    n13.random = n7
    n11.random = n1
    n10.random = n11
    n1.random = n7

    cn7 = s.copyRandomList(n7)
    curr = cn7
    while curr:
        print(f'{curr.val} N={curr.next} R={curr.random}', end=' -> ')
        curr = curr.next
