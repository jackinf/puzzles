from typing import List


class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        split_phrases = [x.split(' ') for x in phrases]

        # naive
        results = []
        for i in range(len(split_phrases)):
            for j in range(len(split_phrases)):
                if i == j:
                    continue
                if split_phrases[i][-1] == split_phrases[j][0]:
                    joined = ' '.join(split_phrases[i] + split_phrases[j][1:])
                    if joined not in results:
                        results.append(joined)

        return sorted(results)