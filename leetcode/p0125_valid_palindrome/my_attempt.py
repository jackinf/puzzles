class Solution:
    """
    https://leetcode.com/problems/valid-palindrome/
    Accepted
    """
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join(x for x in s if x.isalnum()).lower()
        return ss == ss[::-1]

if __name__ == "__main__":
    s = Solution()

    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))