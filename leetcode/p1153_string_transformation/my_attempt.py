from collections import defaultdict


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        N = len(str1)
        if N == 1:
            return True

        dict_list = defaultdict(list)
        dict_list[str1[0]].append(str2[0])
        dict_list[str2[0]].append(str1[0])

        for i in range(1, N):
            if str1[i] == str1[i - 1] and str2[i] == str2[i - 1]:
                pass
                # print(f'{str1[i]} == {str1[i - 1]}, {str2[i]} == {str2[i - 1]}')
            elif str1[i] != str1[i - 1] and str2[i] != str2[i - 1]:
                pass
                # print(f'{str1[i]} != {str1[i - 1]}, {str2[i]} != {str2[i - 1]}')
            else:
                return False

            if str2[i] not in dict_list[str1[i]]:
                dict_list[str1[i]].append(str2[i])
            if str1[i] not in dict_list[str2[i]]:
                dict_list[str2[i]].append(str1[i])

        print(dict_list)
        # todo check if dict list has a possible connection (maybe DFS can help?)

        return True


if __name__ == "__main__":
    s = Solution()
    # print(s.canConvert("leetcode", "codeleet"))
    print(s.canConvert("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"))