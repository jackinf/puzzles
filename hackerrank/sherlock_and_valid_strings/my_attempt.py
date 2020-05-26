#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

"""
Almost valid - 2 test cases are failing
"""
def isValid(s):
    if not s:
        return "YES"
    counter1 = Counter(s)
    counter2 = Counter(counter1.values())
    most_common = counter2.most_common()
    if len(most_common) > 2:
        return "NO"
    if len(most_common) == 1:
        return "YES"
    k1, v1 = most_common.pop(0)
    k2, v2 = most_common.pop(0)
    kdiff = abs(k2 - k1)
    return "YES" if v2 == 1 and kdiff == 1 else "NO"


if __name__ == '__main__':
    # s = input()
    s = "abcdd"
    result = isValid(s)
    print(result)
