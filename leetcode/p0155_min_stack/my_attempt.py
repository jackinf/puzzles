import heapq


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.heap = []
        self.to_remove = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        heapq.heappush(self.heap, x)

    def pop(self) -> None:
        item = self.stack.pop()
        heapq.heappush(self.to_remove, item)

        while self.to_remove and self.heap and self.to_remove[0] == self.heap[0]:
            heapq.heappop(self.to_remove)
            heapq.heappop(self.heap)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        if self.heap:
            return self.heap[0]
        return -1

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()