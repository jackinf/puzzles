# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        st = []
        head = None
        curr, prev = root, Node(None)

        while st or curr:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                curr = st.pop()
                right = curr.right

                # action
                if not head:
                    head = curr

                prev.right, curr.left = curr, prev
                prev = curr

                curr = right

        prev.right, head.left = head, prev
        return head


if __name__ == "__main__":
    s = Solution()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n2.left = n1
    n2.right = n3
    n4.left = n2
    n4.right = n5

    res = s.treeToDoublyList(n4)
    f = res.val
    curr = res

    print("RIGHT")
    print(f'{f}->',end="")
    while True:
        curr = curr.right
        if curr.val == f:
            print(curr.val)
            break
        print(f'{curr.val}->', end="")

    print('LEFT')
    print(f'{f}->',end="")
    while True:
        curr = curr.left
        if curr.val == f:
            print(curr.val)
            break
        print(f'{curr.val}->', end="")