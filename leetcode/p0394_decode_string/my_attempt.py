class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        p_curr = 0
        while p_curr < len(s):
            if s[p_curr] == '[':
                stack.append(p_curr)
            elif s[p_curr] == "]":
                p1 = stack.pop()

                num_len = 0
                while p1 - num_len - 1 >= 0 and s[p1 - num_len - 1].isdigit():
                    num_len += 1

                res_num = int(s[p1 - num_len:p1])
                res_chars = s[p1 + 1:p_curr]
                res = res_num * res_chars
                s = s[:p1 - num_len] + res + s[p_curr + 1:]

                p_curr += len(res) - (len(res_chars) + 2 + num_len)
                continue

            p_curr += 1
        return s