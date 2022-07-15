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


################################

def fibonacci_iter_func():
    first = 0
    second = 1
    while True:
        first, second = second, first + second
        yield second

for item in fibonacci_iter_func():
    print(item)
    time.sleep(1)


###############################

class MyIter2:
    def __iter__(self):
        for item in range(5):
            yield item
        raise StopIteration

a = MyIter2()

for i in a:
    print(i)