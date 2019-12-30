import collections


class Solution:
    # You are given a string, s, and a list of words, words, that are all of the same length. Find all starting
    # indices of substring(s) in s that is a concatenation of each word in words exactly once and without any
    # intervening characters.
    def findSubstring(self, s, words):
        if not words:
            return []

        out = []
        words_dict = collections.Counter(words)

        words_len, word_len = len(words), len(words[0])
        for i in range(len(s) - words_len * word_len + 1):
            seen = {}
            for j in range(words_len):
                t = s[i + j * word_len:i + (j + 1) * word_len]
                if t not in words_dict:
                    break

                seen[t] = seen.get(t, 0) + 1
                if seen[t] > words_dict[t]:
                    break
                if j == words_len - 1:
                    out.append(i)
        return out


print(Solution().findSubstring("barbarfoothefoobarman", ["foo", "bar"]))
