#!/bin/python3


def maxSubsetSum(arr):
    if len(arr) <= 2:
        return max(arr)
    sums = [float('-inf')]*len(arr)
    sums[0] = arr[0]
    sums[1] = max(arr[0], arr[1])
    curr_max_val = max(sums)
    for i in range(2, len(arr)):
        sums[i] = max(arr[i], arr[i] + sums[i-2], curr_max_val)
        curr_max_val = max(sums[i], curr_max_val)
    return curr_max_val


if __name__ == '__main__':
    print(maxSubsetSum([-1, -4, -7, -2]))
    print(maxSubsetSum([3, 7, 4, 6, 5]))
    print(maxSubsetSum([2, 1, 5, 8, 4]))
    print(maxSubsetSum([3, 5, -7, 8, 10]))
