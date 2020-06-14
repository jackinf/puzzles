from bisect import bisect
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        cur, ans = '', []
        for char in searchWord:
            cur += char
            i = bisect.bisect_left(products, cur)
            ans.append([product for product in products[i: i + 3] if product.startswith(cur)])
        return ans


if __name__ == "__main__":
    print(Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))