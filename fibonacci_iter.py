import time

class FibonacciIter:
    def __init__(self):
        self.prev_1 = 0
        self.prev_2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        value = self.prev_1
        self.prev_1, self.prev_2 = self.prev_2, self.prev_1 + self.prev_2
        return value

fibonacci_iter = FibonacciIter()
for item in fibonacci_iter:
    print(item)
    time.sleep(1)