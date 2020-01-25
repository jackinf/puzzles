class LRUCache:
    """
    Accepted (but slow)
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.indexes = []

    def get(self, key: int) -> int:
        if key in self.dict:
            self.indexes.pop(self.indexes.index(key))
            self.indexes.append(key)
            return self.dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.indexes:
            self.indexes.pop(self.indexes.index(key))
            self.indexes.append(key)
            self.dict[key] = value
            return

        if len(self.indexes) >= self.capacity:
            key_to_remove = self.indexes.pop(0)
            del self.dict[key_to_remove]

        if key not in self.indexes:
            self.indexes.append(key)

        self.dict[key] = value


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