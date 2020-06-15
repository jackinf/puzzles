class Solution:
    def solve(self, alphabet, sentence):
        mappings = {}
        for i, ch in enumerate(alphabet):
            mappings[ch] = i
        sentence2 = [(tuple([mappings[ch] for ch in item]), item) for item in sentence]
        sentence2.sort(key=lambda x: x[0])
        return [item[1] for item in sentence2]


if __name__ == "__main__":
    alphabet = ["b", "c", "a"]
    sentence = ["aa", "ab", "bc", "abc", ""]
    print(Solution().solve(alphabet, sentence))  # "", "bc", "ab", "abc", "aa"