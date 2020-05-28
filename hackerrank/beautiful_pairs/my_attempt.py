#!/bin/python3

from collections import Counter


def beautifulPairs(A, B):
    aa = Counter(A)
    ans, offset = 0, -1
    for i in range(len(B)):
        if B[i] in aa and aa[B[i]] > 0:
            aa[B[i]] -= 1
            ans += 1
        else:
            offset = 1
    return ans + offset


if __name__ == '__main__':
    print(beautifulPairs(
        [1, 2, 3, 4],
        [1, 2, 3, 3]
    ))
    print(beautifulPairs(
        [3, 5, 7, 11, 5, 8],
        [5, 7, 11, 10, 5, 8]
    ))