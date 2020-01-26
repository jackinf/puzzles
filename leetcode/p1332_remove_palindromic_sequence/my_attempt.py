class Solution:
    def removePalindromeSub(self, s: str) -> int:
        cache = []
        word_len = N = len(s)

        while word_len > 0:
            for i in range(0, N - word_len + 1):
                sub_s = s[i:i + word_len]
                if sub_s == sub_s[::-1]:
                    cache.append(sub_s)
            word_len -= 1
        print(cache)

        count = 0
        for item in cache:
            if len(s) == 0:
                break

            if item in s:
                start_i = s.index(item)
                end_i = start_i + len(item)
                s = s[0:start_i:] + s[end_i:]
                count += 1

        # special case: same letters count as a palindromic sequence.
        if count > 2:
            return 2

        if len(s) != 0:
            raise Exception("should be empty s")

        return count


if __name__ == "__main__":
    s = Solution()

    print(s.removePalindromeSub("ababa"))
    print(s.removePalindromeSub("abb"))
    print(s.removePalindromeSub("baabb"))
    print(s.removePalindromeSub("bbaabaaa"))