class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.flatten_inner(head)
        return head

    def flatten_inner(self, head: 'Node') -> 'Node':
        curr = head
        tail = head
        while curr:
            nexxt = curr.next
            last_node = curr.next
            if curr.child:
                last_node = self.flatten_inner(curr.child)

                # bind current with the child
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None

                # bind child's last element
                if nexxt:
                    last_node.next = nexxt
                    nexxt.prev = last_node

            if last_node:
                tail = nexxt if nexxt else last_node
            curr = nexxt
        return tail