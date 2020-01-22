from typing import List


class Solution:
    """
    My solution was accepted
    """

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a_rotations, a_rotations_rev = self.find(A[0], zip(A, B))
        b_rotations, b_rotations_rev = self.find(B[0], zip(B, A))

        if a_rotations != -1 and b_rotations != -1:
            print('ab_rotations', a_rotations, a_rotations_rev, b_rotations, b_rotations_rev)
            return min(a_rotations, a_rotations_rev, b_rotations, b_rotations_rev)
        elif b_rotations != -1:
            print('b_rotations', b_rotations, b_rotations_rev)
            return min(b_rotations, b_rotations_rev)
        elif a_rotations != -1:
            print('a_rotations', a_rotations, a_rotations_rev)
            return min(a_rotations, a_rotations_rev)

        return -1

    def find(self, current: int, ABzip):
        rotations = 0
        reverse_rotations = 0
        for i, (current_item, other_item) in enumerate(ABzip, 1):
            if other_item == current and current_item != current:
                rotations += 1
            elif current_item != current:
                return -1, -1
            elif other_item != current:
                reverse_rotations += 1
        return rotations, reverse_rotations


if __name__ == "__main__":
    s = Solution()
    A1, B1 = (
        [2,1,6,4,2,2],
        [5,2,2,2,3,2],
    )

    with open('test_case_2.txt', 'r') as f:
        A2, B2 = (
            [int(x) for x in f.readline().split(',')],
            [int(x) for x in f.readline().split(',')],
        )

    print(s.minDominoRotations(A2, B2))