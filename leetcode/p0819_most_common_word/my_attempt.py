from collections import Counter
import re
from typing import List


class Solution:
    """
    Accepted
    """
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = Counter(re.split('[^a-zA-Z]', paragraph.lower()))
        for word, count in words.most_common():
            if word and word not in banned:
                return word
        return ""


if __name__ == "__main__":
    print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))