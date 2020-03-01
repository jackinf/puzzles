from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict1 = {}
        self.dict2 = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict1[(key, timestamp)] = value
        self.dict2[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict2[key]
        p1, p2 = 0, len(arr) - 1

        while p1 <= p2:
            m = p1 + (p2 - p1) // 2
            if arr[m] == timestamp:
                return self.dict1[(key, arr[m])]
            elif arr[m] < timestamp:
                p1 = m + 1
            elif arr[m] > timestamp:
                p2 = m - 1
        if p1 == 0:
            return ""
        return self.dict1[(key, arr[p1 - 1])]