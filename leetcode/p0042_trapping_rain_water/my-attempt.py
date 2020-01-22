from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0

        res_arr = [{"curr": height[0], "min": None, "max": None}]

        def fix_all_previous_items():
            for arr_item in res_arr:
                if arr_item["curr"] is None and arr_item["max"] is not None:
                    arr_item["curr"] = arr_item["max"]

        def scan(arr, start_from):
            prev_max_height = -1
            prev_max_height_i = -1
            for i in range(start_from, n):
                if height[i] > height[i - 1] and prev_max_height <= height[i]:
                    prev_max_height = -1
                    prev_max_height_i = -1

                    arr.append({"curr": height[i], "min": None, "max": None})
                    fix_all_previous_items()

                elif height[i] == height[i - 1]:
                    arr.append({"curr": height[i], "min": None, "max": None})

                else:  # previous item is bigger than the current one
                    if prev_max_height == -1:
                        prev_max_height = height[i - 1]
                        prev_max_height_i = i - 1
                    arr.append({"curr": None, "min": height[i], "max": prev_max_height})

            fix_all_previous_items()

            # check if loop did not happen at all
            if n <= start_from:
                arr.append({"curr": None, "min": height[-1], "max": height[-1]})

            return prev_max_height_i

        last_highest_i = 0
        while True:
            last_highest_i = scan(res_arr, last_highest_i+1)
            if last_highest_i == -1:
                res_arr[-1]["curr"] = height[-1]
                break

            last_highest_i += 1
            res_arr = res_arr[:last_highest_i]

            print([x["curr"] for x in res_arr], last_highest_i)
        print([x["curr"] for x in res_arr], last_highest_i)

        sum = 0
        for i in range(n):
            sum += res_arr[i]["curr"] - height[i]
        return sum

if __name__ == "__main__":
    s = Solution()
    # print(s.trap([0,1,0,2,3,4,5,2,7,4]))
    # print(s.trap([0,1,0,2,3,4,5,2,7,4]))
    # print(s.trap([0,1,0,2,1,3,2,99,1]))
    # print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.trap([4, 2, 3]))