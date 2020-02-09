from typing import List


class Solution:
    def quicksort(self, arr: List[int], low: int, high: int):
        if low < high:
            pi = self.partition_last(arr, low, high)

            self.quicksort(arr, low, pi-1)
            self.quicksort(arr, pi+1, high)

    @staticmethod
    def partition_last(arr: List[int], low: int, high: int) -> int:
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    @staticmethod
    def partition_first(arr: List[int], low: int, high: int) -> int:
        i = low + 1
        pivot = arr[low]

        for j in range(low, high+1):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        i -= 1
        arr[i], arr[low] = arr[low], arr[i]
        return i

if __name__ == "__main__":
    s = Solution()

    arr1 = [1, 8, 3, 9, 4, 5, 7]
    s.quicksort(arr1, 0, len(arr1)-1)
    print(arr1)