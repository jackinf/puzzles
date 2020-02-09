from typing import List


class Solution():
    def quickselect(self, arr: List[int], low: int, high: int, k: int) -> int:
        if low == high:
            return arr[high]

        pi = self.partition(arr, low, high)
        if k == pi:
            return arr[k]
        elif k > pi:
            return self.quickselect(arr, pi+1, high, k)
        else:
            return self.quickselect(arr, low, pi-1, k)

    def partition(self, arr: List[int], low: int, high: int) -> int:
        i = low-1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        i += 1
        arr[high], arr[i] = arr[i], arr[high]
        return i


if __name__ == "__main__":
    s = Solution()
    arr1 = [1, 8, 3, 9, 4, 5, 7]
    N = len(arr1)
    print(s.quickselect(arr1, 0, N-1, N-3))
