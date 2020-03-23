from typing import List


class Solution:
    """
    Accepted
    """
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.s = s
        self.res = []
        self.solve(0, [])
        return self.res

    def solve(self, start: int, points: List[int]):
        if len(points) == 2 and len(self.s) - start > 7 or len(points) == 1 and len(self.s) - start > 10:
            return

        if len(points) == 3:
            p1, p2, p3 = points
            part1, part2, part3, part4 = self.s[:p1 + 1], self.s[p1 + 1:p2 + 1], self.s[p2 + 1:p3 + 1], self.s[p3 + 1:]
            if not part1 or not part2 or not part3 or not part4:
                return

            part1, part2, part3, part4 = int(part1), int(part2), int(part3), int(part4)
            ip = f'{part1}.{part2}.{part3}.{part4}'
            print(ip)
            if len(ip) - 3 != len(self.s):
                return

            valid = all([0 <= int(part) <= 255 for part in [part1, part2, part3, part4]])
            if valid:
                self.res.append(ip)
            return

        for i in range(start, len(self.s)):
            prev_point = points[-1] if points else -1
            if i - prev_point > 3:
                return
            points.append(i)
            self.solve(i, points)
            points.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
    print(s.restoreIpAddresses("0000"))
    print(s.restoreIpAddresses("255255255255"))