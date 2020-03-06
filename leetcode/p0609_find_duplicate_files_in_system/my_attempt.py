from collections import defaultdict
from typing import List


class Solution:
    """
    Accepted
    """
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)

        for path in paths:
            path_items = path.split(' ')
            directory, files = path_items[0], path_items[1:]

            for file in files:
                p1, p2 = file.find('('), file.rfind(')')
                dict1[file[p1 + 1:p2]].append(directory + '/' + file[:p1])

        return [value for value in dict1.values() if len(value) >= 2]
