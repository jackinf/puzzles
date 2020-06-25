import threading


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.q = []
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)

    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.q.append(element)
        self.pulling.release()

    def dequeue(self) -> int:
        self.pulling.acquire()
        res = self.q.pop(0)
        self.pushing.release()
        return res

    def size(self) -> int:
        return len(self.q)
