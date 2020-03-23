from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def to_bin(num: int):
            return "{0:8b}".format(num)

        while data:
            elem = to_bin(data.pop(0))
            if elem[0] in ["0", " "]:
                continue
            elif elem[0:3] == "110":
                if not data or to_bin(data.pop(0))[0:2] != "10":
                    return False
            elif elem[0:4] == "1110":
                for _ in range(2):
                    if not data or to_bin(data.pop(0))[0:2] != "10":
                        return False
            elif elem[0:5] == "11110":
                for _ in range(3):
                    if not data or to_bin(data.pop(0))[0:2] != "10":
                        return False
            else:
                return False
        return True


if __name__ == "__main__":
    print(Solution().validUtf8([197, 130, 1]))
    print(Solution().validUtf8([235, 140, 4]))