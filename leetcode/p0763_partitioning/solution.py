class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i,c in enumerate(S)}
        end = start = 0

        res = []
        for i, c in enumerate(S):
            end = max(end, last[c])
            if i == end:
                res.append(end-start+1)
                start = i + 1
        return res


if __name__ == "__main__":
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))