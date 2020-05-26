#!/bin/python3

import heapq

def runningMedian(arr):
    a, b, res = [], [], []

    for val in arr:
        # Adding
        if not b or val > b[0]: heapq.heappush(b, float(val))
        else: heapq.heappush(a, float(-val))

        # Balancing
        if len(a) - len(b) > 1: heapq.heappush(b, -heapq.heappop(a))
        elif len(b) - len(a) > 1: heapq.heappush(a, -heapq.heappop(b))

        # Retrieval
        if len(a) == len(b): res.append((-a[0] + b[0]) / 2.)
        elif len(a) > len(b): res.append(-a[0])
        else: res.append(b[0])

    return res


if __name__ == '__main__':
    print(runningMedian([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(runningMedian([12, 4, 5, 3, 8, 7]))