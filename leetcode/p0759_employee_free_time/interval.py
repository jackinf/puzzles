class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'[{self.start}, {self.end}]'