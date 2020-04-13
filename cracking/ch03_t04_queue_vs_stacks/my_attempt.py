class MyQueue:
    read_stack = []
    write_stack = []

    def append(self, x):
        self.write_stack.append(x)

    def pop(self):
        if not self.read_stack:
            while self.write_stack:
                self.read_stack.append(self.write_stack.pop())
        if self.read_stack:
            return self.read_stack.pop()
        raise Exception("No items in MyQueue")


if __name__ == "__main__":
    my_queue = MyQueue()
    my_queue.append(1)
    my_queue.append(2)
    print(my_queue.pop())
    my_queue.append(3)
    my_queue.append(4)
    print(my_queue.pop())
    my_queue.append(5)
    print(my_queue.pop())
    print(my_queue.pop())
    print(my_queue.pop())