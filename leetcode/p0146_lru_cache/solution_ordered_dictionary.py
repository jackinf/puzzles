from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return - 1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


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