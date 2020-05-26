from leetcode.p0759_employee_free_time.interval import Interval


class Solution:
    def employeeFreeTime(self, schedule: [[Interval]]) -> [Interval]:
        sch = [x for y in schedule for x in y]
        sch.sort(key=lambda x: x.start)
        res, last = [], float('-inf')

        for interval in sch:
            if interval.start > last != float('-inf'):
                newInterval = Interval(last, interval.start)
                res.append(newInterval)
            last = max(last, interval.end)

        return res


if __name__ == "__main__":
    free_time = Solution().employeeFreeTime([
        [Interval(1, 2),Interval(5,6)],
        [Interval(1,3)],
        [Interval(4,10)]
    ])
    print(free_time)