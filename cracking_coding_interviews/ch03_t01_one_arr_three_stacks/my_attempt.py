class Stacks:
    def __init__(self, stacks: int):
        self.top = [-1] * stacks
        self.offset = list(range(stacks))
        self.arr = [None] * stacks

    def append(self, x, which: int):
        self.top[which] += 1
        if self.top[which] + 1 > self.get_single_stack_size():
            self.resize_array()
        stack_size = self.get_single_stack_size()
        self.arr[self.get_index_of_top_element_in_stack(which, stack_size)] = x

    def pop(self, which: int):
        if self.top[which] == -1:
            raise Exception("No items")
        stack_size = self.get_single_stack_size()
        index = self.get_index_of_top_element_in_stack(which, stack_size)
        item = self.arr[index]
        self.arr[index] = None
        self.top[which] -= 1
        return item

    def get_index_of_top_element_in_stack(self, which: int, stack_size: int):
        return self.offset[which] + self.top[which]

    def get_single_stack_size(self):
        return len(self.arr) // len(self.top)

    def resize_array(self):
        stack_size = self.get_single_stack_size()
        new_arr = [None] * len(self.arr)*2
        for which in range(len(self.arr) // stack_size):
            for i in range(stack_size):
                new_arr[self.offset[which]*2 + i] = self.arr[self.offset[which] + i]
        self.offset = [num*2 for num in self.offset]
        self.arr = new_arr

    def __str__(self):
        return f'{self.arr}'


if __name__ == "__main__":
    st = Stacks(4)
    st.append(1, 0)
    st.append(2, 0)
    st.append(3, 0)
    st.append(10, 1)
    st.append(11, 1)
    st.append(21, 2)
    st.append(22, 2)
    st.append(23, 2)
    print(st)
    print(st.pop(2))
    print(st.pop(2))
    print(st.pop(1))
    print(st)
    st.append(41, 2)
    st.append(42, 2)
    st.append(43, 2)
    st.append(44, 2)
    st.append(45, 2)
    print(st)

