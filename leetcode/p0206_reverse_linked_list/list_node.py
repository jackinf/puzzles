class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return self.__str__()