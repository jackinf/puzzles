import re
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def solve(ss: str, words: List[str], seen):
            if len(seen) >= len(s):
                return len(set(seen)) == len(s)

            for word in words:
                newset = seen[:]
                found_indexes = [m.start() for m in re.finditer(word, ss)]
                for found_index in found_indexes:
                    for index in range(len(word)):
                        newset.append(found_index + index)

                newWordDict = [x for x in words if x != word]
                res = solve(ss, newWordDict, newset)
                if res:
                    return True

            return False

        return solve(s, wordDict, [])


if __name__ == "__main__":
    s = Solution()

    # print(s.wordBreak("leetcode", ["leet","code"]))
    print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
    # print(s.wordBreak("cbca", ["bc","ca"]))