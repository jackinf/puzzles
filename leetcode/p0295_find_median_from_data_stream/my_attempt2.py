class Node:
    def __init__(self, val: int = None, next: 'Node' = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        mid = len(self.arr) // 2
        if self.arr % 2 == 0:
            return (self.arr[mid] + self.arr[mid+1])/2
        return self.arr[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()