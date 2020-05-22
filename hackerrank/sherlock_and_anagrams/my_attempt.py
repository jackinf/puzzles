#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    N = len(s)
    counter = 0
    for m in range(1, N):
        prep = []
        for i in range(N-m+1):
            prep.append(Counter(s[i:i+m]))
        print(prep, m)
        while prep:
            item1 = prep.pop(0)
            for item2 in prep:
                if item1 == item2:
                    counter += 1
    return counter


if __name__ == '__main__':
    s = "abba"
    result = sherlockAndAnagrams(s)
    print(result)
