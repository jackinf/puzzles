from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            email2 = []
            for i in range(len(email)):
                ch = email[i]
                if ch == ".":
                    continue
                if ch == "+" or ch == "@":
                    email2.extend(email[email.index("@"):])
                    break
                email2.append(ch)
            result.add("".join(email2))
        return len(result)