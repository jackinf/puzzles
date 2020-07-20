from typing import List, Union


class Node:
    def __init__(self, val: int, left: Union['Node', None] = None, right: Union['Node', None] = None):
        self.val = val
        self.left = left
        self.right = right


def build(node_vals: List[int]) -> Node:
    head = Node(node_vals.pop(0))
    q = [head]
    while q and node_vals:
        curr = q.pop(0)
        leftval = node_vals.pop(0)
        if leftval:
            n = Node(leftval)
            curr.left = n
            q.append(n)

        rightval = node_vals.pop(0)
        if rightval:
            n = Node(rightval)
            curr.right = n
            q.append(n)
    return head


def preorder(node: Node) -> List[int]:
    res = []
    st = [node]
    while st:
        curr = st.pop()
        res.append(curr.val)
        if curr.right:
            st.append(curr.right)
        if curr.left:
            st.append(curr.left)
    return res


def postorder(node: Node) -> List[int]:
    res = []
    st = [node]
    while st:
        curr = st.pop()
        res.append(curr.val)
        if curr.left:
            st.append(curr.left)
        if curr.right:
            st.append(curr.right)
    return list(reversed(res))


def inorder(node: Node) -> List[int]:
    res = []
    st = []
    curr = node

    while st or curr:
        if curr:
            st.append(curr)
            curr = curr.left
        else:
            curr = st.pop()
            res.append(curr.val)
            curr = curr.right

    return res

"""
        -10
    9         20
          15       7
"""
if __name__ == "__main__":
    node_vals = [-10,9,20,None,None,15,7]
    head = build(node_vals)
    print(preorder(head))
    print(postorder(head))
    print(inorder(head))