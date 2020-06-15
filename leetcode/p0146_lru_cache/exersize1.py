class Node:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None

class LRUCache:
    def _add_node(self, node) :
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> Node:
        node = self.tail.prev
        self._remove_node(node)
        return node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head, self.tail = Node(), Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int):
        node = self.cache.get(key, None)
        if not node: return -1
        self._move_to_head(node)
        return node.val

    def put(self, key: int, val: int):
        node = self.cache.get(key, None)
        if node:
            node.val = val
            self._move_to_head(node)
        else:
            newNode = Node()
            newNode.key = key
            newNode.val = val

            self.cache[key] = newNode
            self.size += 1
            self._add_node(newNode)

            if self.size > self.capacity:
                t = self._pop_tail()
                del self.cache[t.key]
                self.size -= 1


if __name__ == "__main__":
    cache = LRUCache(2)

    operations_1 = ["LRUCache", "put", "put", "put", "put", "get", "get"]
    values_1 = [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
    expected_output_1 = [-1, 3]

    cache = None
    for i, operation in enumerate(operations_1):
        if operation == "LRUCache":
            cache = LRUCache(values_1[i][0])
        elif operation == "put":
            cache.put(values_1[i][0], values_1[i][1])
        elif operation == "get":
            res = cache.get(values_1[i][0])
            print(f"{res} == {expected_output_1.pop(0)}")