from collections import defaultdict
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        s = logs[0].split(':')
        stack.append(int(s[0]))
        i, prev = 1, int(s[2])

        while i < len(logs):
            s = logs[i].split(":")
            the_id, the_time = int(s[0]), int(s[2])
            if s[1] == "start":
                if stack:
                    print(res, the_time, prev)
                    res[stack[-1]] += the_time - prev
                stack.append(the_id)
                prev = the_time
            else:
                res[stack[-1]] += the_time - prev + 1
                stack.pop()
                prev = the_time + 1
            i += 1