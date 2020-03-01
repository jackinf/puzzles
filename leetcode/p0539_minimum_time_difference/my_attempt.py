from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        MAX_MINS = 1440
        timePointsConverted = []
        for timePoint in timePoints:
            hh, mm = timePoint.split(':')
            mmm = int(hh) * 60 + int(mm)
            timePointsConverted.append(mmm)

        timePointsConverted.sort()

        diff = float('inf')
        for i in range(len(timePointsConverted) - 1):
            curr1 = timePointsConverted[i]
            next1 = timePointsConverted[i + 1]
            res = abs(curr1 - next1)
            diff = min(diff, res, MAX_MINS - res)

        if len(timePointsConverted) > 2:
            curr1 = timePointsConverted[-1]
            next1 = timePointsConverted[0]
            res = abs(curr1 - next1)
            diff = min(diff, res, MAX_MINS - res)

        return diff