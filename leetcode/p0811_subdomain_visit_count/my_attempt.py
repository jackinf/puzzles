from collections import defaultdict
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)
        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split(' ')
            count = int(count_str)

            while "." in domain:
                counter[domain] += count
                domain = domain[domain.index('.') + 1:]
            counter[domain] += count

        return [f"{v} {k}" for k, v in counter.items()]


if __name__ == "__main__":
    print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))