#!/bin/python3

import os
import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "[{0}, l:{1}, r:{2}]".format(self.val, self.left.val if self.left else "-", self.right.val if self.right else "-")


def build_tree(root, indexes):
    arr = [root]
    while arr:
        node = arr.pop(0)
        left, right = indexes.pop(0)
        node.left = Node(left) if left != -1 else None
        node.right = Node(right) if right != -1 else None
        if node.left: arr.append(node.left)
        if node.right: arr.append(node.right)


def build_levels(node, levels, level):
    if not node:
        return
    if len(levels) <= level:
        levels.append([])
    levels[level].append(node)
    build_levels(node.left, levels, level + 1)
    build_levels(node.right, levels, level + 1)


def inorder(node, res):
    if not node:
        return
    inorder(node.left, res)
    res.append(node.val)
    inorder(node.right, res)


def swapNodes(indexes, queries):
    root, results, levels = Node(1), [], []

    build_tree(root, indexes)
    build_levels(root, levels, 0)

    # for i, level in enumerate(levels):
    #     print("LEVEL {}".format(i))
    #     print(level)

    for k in queries:
        for kk in range(0, len(levels), k):
            for node in levels[kk - 1]:
                node.left, node.right = node.right, node.left
        res = []
        inorder(root, res)
        results.append(res)

    return results


if __name__ == '__main__':
    indexes = [
        [2, 3],
        [4, 5],
        [6, -1],
        [-1, 7],
        [8, 9],
        [10, 11],
        [12, 13],
        [-1, 14],
        [-1, -1],
        [15, -1],
        [16, 17],
        [-1, -1],
        [-1, -1],
        [-1, -1],
        [-1, -1],
        [-1, -1],
        [-1, -1]
    ]

    queries = [2, 3]
    result = swapNodes(indexes, queries)
    for row in result:
        print(" ".join([str(x) for x in row]))
