#!/bin/python3

# Complete the candies function below.
def candies(arr):
    res = 0
    dp1 = [1]*len(arr)
    dp2 = [1]*len(arr)
    for i in range(1, len(arr)):
        dp1[i] = 1 if arr[i] <= arr[i-1] else dp1[i-1]+1
    for i in range(len(arr)-2, -1, -1):
        dp2[i] = 1 if arr[i] <= arr[i+1] else dp2[i+1]+1
    print(dp1, dp2)
    for i in range(len(arr)):
        res += max(dp1[i], dp2[i])
    return res


if __name__ == '__main__':
    print(candies([1, 2, 2]))
    print(candies([2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))
    print(candies([2, 4, 3, 5, 2, 6, 4, 5]))

