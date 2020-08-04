class Solution:
    """ Accepted """
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        res = []
        ss = S.replace("-", "")[::-1]
        for i in range(0, len(ss), K):
            res.append(ss[i:i + K])
        return "-".join(res).upper()[::-1]
