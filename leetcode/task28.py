class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            for j, c in enumerate(needle):
                if haystack[i + j] != c:
                    break
            else:
                return i
        return -1

    def strStr1(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1

        def search(hay: str, nee: str, i, found_i):
            if len(nee) == 0:
                return found_i
            if len(hay) == 0:
                return -1

            if hay[0] == nee[0]:
                found_i = i if found_i == -1 else found_i
                return search(hay[1:], nee[1:], i+1, found_i)
            else:
                if found_i == -1:
                    return search(hay[1:], needle, i+1, -1)
                else:
                    next_index = found_i + 1 if len(haystack) > found_i else len(haystack) -1
                    return search(haystack[next_index:], needle, next_index, -1)
        found = search(haystack, needle, 0, -1)
        return found


print(Solution().strStr('hello', 'll'))
print(Solution().strStr('ababcd', 'abc'))
print(Solution().strStr('hellhellhelloo', 'hello'))
print(Solution().strStr('a', 'aa'))
print(Solution().strStr('mississippi', 'issip'))
print(Solution().strStr('mississippi', 'issipi'))
