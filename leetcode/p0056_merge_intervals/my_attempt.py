from typing import List


class Solution:
    """
    Accepted
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # print(intervals)

        while True:
            merged = False
            for i in range(len(intervals)):
                for j in range(i+1, len(intervals)):
                    [i_start, i_end] = intervals[i]
                    [j_start, j_end] = intervals[j]
                    if i_end < j_start:
                        continue
                    merged = True
                    intervals[i] = [min(i_start, j_start), max(j_end, i_end)]
                    intervals.pop(j)
                    break
                if merged:
                    break
            if not merged:
                break
        return intervals



if __name__ == "__main__":
    s = Solution()

    input_1 = [[1,3],[2,6],[8,10],[15,18]]
    input_2 = [[1,4],[0,2],[3,5]]
    print(s.merge(input_1))  # output: [[1,6],[8,10],[15,18]]
    print(s.merge(input_2))

