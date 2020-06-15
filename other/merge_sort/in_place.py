from typing import List


class Solution:
    def mergeSort(self, arr: List[int], start, end):
        if end - start > 1:
            mid = (start+end)//2
            self.mergeSort(arr, start, mid)
            self.mergeSort(arr, mid, end)
            self.merge(arr, start, mid, end)

    def merge(self, arr: List[int], start: int, mid: int, end: int):
        L = arr[start:mid]
        R = arr[mid:end]
        i = 0
        j = 0
        k = start

        def incrementLeft(i):
            arr[l] = L[i]
            return i + 1

        def incrementRight(j):
            arr[l] = R[j]
            return j + 1

        for l in range(k, end):
            if len(L) > i and len(R) > j:
                if L[i] < R[j]:
                    i = incrementLeft(i)
                else:
                    j = incrementRight(j)
            else:
                if j >= len(R) and i < len(L):
                    i = incrementLeft(i)
                elif i >= len(L) and j < len(R):
                    j = incrementRight(j)


if __name__ == "__main__":
    arr1 = [1, 8, 3, 6, 4, 5, 7, 2]
    Solution().mergeSort(arr1, 0, len(arr1))
    print(arr1)