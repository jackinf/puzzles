# import re
# [m.start() for m in re.finditer('test', 'test test test test')]
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(ss: str, dict1: List[str]) -> bool:
            if len(ss) == 0:
                return True

            for word in dict1:
                res = dfs(ss.replace(word, ""), [x for x in dict1 if x != word])
                if res:
                    return True

            return False

        return dfs(s, wordDict)


if __name__ == "__main__":
    s = Solution()

    print(s.wordBreak("cbca", ["bc","ca"]))