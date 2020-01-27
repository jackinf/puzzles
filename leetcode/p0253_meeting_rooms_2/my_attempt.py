from typing import List


class Solution:
    """
    Accepted
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        r_endtimes: List[int] = []  # end times of rooms

        for interval in intervals:
            found = False
            for r_endtime_i, r_endtime in enumerate(r_endtimes):
                if r_endtime <= interval[0]:
                    r_endtimes[r_endtime_i] = interval[1]
                    found = True
                    break

            if not found:
                r_endtimes.append(interval[1])

        return len(r_endtimes)


if __name__ == "__main__":
    s = Solution()

    print(s.minMeetingRooms([[7,10],[2,4]]))
    print(s.minMeetingRooms([[0,30],[5,10],[15,20]]))