from tasks.coin_collector.solution import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_case1(self):
        components = [(1, 1), (0, 0)]
        player = [1, 0]
        self.assertEqual('NPWSP', Solution().solve(components, player))

    def test_case2(self):
        components = [(1, 1), (0, 1)]
        player = [0, 2]
        self.assertEqual('ESPWP', Solution().solve(components, player))

    def test_case3(self):
        components = [(1, 0), (2, 2), (0, 3)]
        player = [1, 1]
        self.assertEqual('SPENNPWWNP', Solution().solve(components, player))

    def test_case4(self):
        components = [(5, 4), (6, 6), (1, 0), (0, 5), (5, 1)]
        player = [4, 6]
        self.assertEqual('ESSPENNPWWWWWSSSSSSPWNNNNNPEEEEESSSSP', Solution().solve(components, player))


if __name__ == "__main__":
    unittest.main()