from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        num_q, str_q = [], []

        for log in logs:
            log_arr = log.split(' ')
            if log_arr[1].isnumeric():
                num_q.append(log)
            else:
                modified = " ".join(log_arr[1:] + [log_arr[0]])
                str_q.append((modified, log))

        str_q.sort()
        original_str_q = [x[1] for x in str_q]
        return original_str_q + num_q