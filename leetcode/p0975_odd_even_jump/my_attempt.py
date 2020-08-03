from collections import defaultdict
from typing import List, Dict


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


"""
How I thought:
1. create sorted array
2. create nodes out of the sorted array, 
	2.1 create node
	2.2 connect the node to previous
	2.3 store them in arr_sorted_map defaultdict(list), where {val: [Node]}
3. traverse arr
	3.1 pop(0) the node from arr_sorted_map -> node
	3.2 odds[node] = node.next if node.next, evens[node] = node.prev if node.prev
	3.3 break connection between nodes
4. BFS
	4.1 for each element in odds, start with queue
		4.1.0 while queue is not empty:
		4.1.1 if last element -> append current score to final result, break
		4.1.2 if seen -> break, else delete
		4.1.3 on every odd step +1 to current score
	4.2 do the same but evens become odds and vice versa
"""


class Solution:
    """ I get wrong answers """

    def oddEvenJumps(self, A: List[int]) -> int:
        if not A:
            return 0

        a_sorted = sorted(A)
        dd = self.create_nodes(a_sorted)
        odds, evens, last = self.create_odd_even_maps(A, dd)
        total_score1 = self.count_scores(odds.copy(), evens.copy(), last)
        total_score2 = self.count_scores(evens.copy(), odds.copy(), last)
        total_score = total_score1 + total_score2
        return total_score + 1

    def create_nodes(self, a_sorted: List[int]) -> Dict:
        dd = defaultdict(list)
        prev = None
        for num in a_sorted:
            node = Node(num)
            if not prev:
                prev = node
            else:
                prev.next = node
                node.prev = prev
                prev = node
            dd[node.val].append(node)
        return dd

    def create_odd_even_maps(self, arr: List[int], dd: Dict):
        odds, evens, node = {}, {}, None
        for num in arr:
            node = dd[num].pop(0)
            if node.next:
                odds[node] = node.next
                node.next.prev = node.prev
            if node.prev:
                evens[node] = node.prev
                node.prev.next = node.next
        return odds, evens, node

    def count_scores(self, odds, evens, last):
        seen = set()
        total_score = 0
        st = [(node, 1, 0) for node in odds.keys()]
        while st:
            curr, depth, score = st.pop()
            if curr is last:
                total_score += score
                continue
            if curr in seen:
                continue
            seen.add(curr)
            if depth % 2 == 0 and curr in evens:
                st.append((evens[curr], depth + 1, score))
            elif curr in odds:
                st.append((odds[curr], depth + 1, score + 1))
        return total_score


if __name__ == "__main__":
    A1 = [11, 33, 11, 22]
    A2 = [10, 13, 12, 14, 15]
    A3 = [2, 3, 1, 1, 4]
    print(Solution().oddEvenJumps(A3))
