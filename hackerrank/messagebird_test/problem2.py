# Programmer string: find letters between programmer strings
from collections import Counter


def solve(s):
    N = len(s)
    if N < len("programmer"):
        return 0

    start_index = find(s)
    end_index = N - find(s[::-1])
    diff = end_index - start_index
    return max(0, diff)


def find(s):
    counter = Counter("programmer")
    to_find = len("programmer")
    for i in range(len(s)):
        letter = s[i]
        if counter[letter] <= 0:
            continue
        counter[letter] -= 1
        to_find -= 1
        if to_find == 0:
            return i + 1
    return i+1


if __name__ == "__main__":
    print(solve("xprogxramremxrprogrammxer"))  # 2