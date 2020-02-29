class Node:
    def __init__(self, val: int = None, next: 'Node' = None, prev: 'Node' = None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.val)


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head: Node = None
        self.median: Node = None
        self.count: int = 0

    def addNum(self, num: int) -> None:
        curr = self.head
        trav_count = 0
        if not curr or curr.val > num:
            self.median = self.head = Node(num, curr)
        else:
            while True:
                trav_count += 1
                if not curr.next:
                    curr.next = Node(num, prev=curr)
                    break
                if curr.next.val > num:
                    curr.next = Node(num, next=curr.next, prev=curr)
                    break
                curr = curr.next

        even = self.count % 2 == 0
        med_count = self.count // 2
        if med_count < trav_count and even and self.median.next:
            self.median = self.median.next
        elif med_count >= trav_count and not even and self.median.prev:
            self.median = self.median.prev

        self.count += 1

    def findMedian(self) -> float:
        if not self.head:
            return 0

        if self.count % 2 == 0:
            return (self.median.val + self.median.next.val) / 2
        return self.median.val


        # curr = self.head
        # to_traverse = self.count // 2
        # while True:
        #     to_traverse -= 1
        #     if to_traverse <= 0:
        #         break
        #     curr = curr.next
        #
        # if self.count % 2 == 0:  # is number even?
        #     return (curr.val + curr.next.val) / 2
        # if not curr.next:
        #     return curr.val
        # return curr.next.val


if __name__ == "__main__":
    s = MedianFinder()
    s.addNum(-1)
    print(s.findMedian())
    s.addNum(-2)
    print(s.findMedian())
    s.addNum(-3)
    print(s.findMedian())
    s.addNum(-4)
    print(s.findMedian())
    s.addNum(-5)
    print(s.findMedian())
