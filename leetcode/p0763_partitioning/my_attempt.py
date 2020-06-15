from typing import List


class Solution:
    """
    Accepted
    """
    def partitionLabels(self, S: str) -> List[int]:

        # step 1: construct intervals
        intervals = {}
        for i, letter in enumerate(S):
            if letter in intervals:
                intervals[letter][1] = i
            else:
                intervals[letter] = [i, i]

        # step 2: merge intervals
        combs = []

        for s, e in intervals.values():
            if not combs:
                combs.append((s, e))
                continue

            ls, le = combs[-1]
            if le > s:
                combs[-1] = (ls, max(e, le))
            else:
                combs.append((s, e))

        # calculate length of the intervals
        return [e - s + 1 for s, e in combs]


if __name__ == "__main__":
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))  # should give [9,7,8]