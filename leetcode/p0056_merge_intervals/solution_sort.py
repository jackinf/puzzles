from typing import List


class Pair:
    def __init__(self, arr: List[int]):
        self.start = arr[0]
        self.end = arr[1]

    def __repr__(self):
        return f'({self.start},{self.end})'


class Solution:
    def merge(self, intervals: List[Pair]):
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged


if __name__ == "__main__":
    s = Solution()

    input_1 = [Pair([1,3]),Pair([2,6]),Pair([8,10]),Pair([15,18])]
    input_2 = [Pair([1,4]),Pair([0,2]),Pair([3,5])]
    print(s.merge(input_1))  # output: [[1,6],[8,10],[15,18]]
    print(s.merge(input_2))

