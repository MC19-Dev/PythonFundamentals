class FibonacciIterator:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.count = 0
        self.value = 1
        self.prev = 0

        return self

    def __next__(self):
        if self.count < self.n:
            value = self.value
            self.value += self.prev
            self.prev = value
            self.count += 1
            
            return value
        else:
            raise StopIteration


fib_instance = FibonacciIterator(10)
fib_iter = iter(fib_instance)

for nr in fib_iter:
    print(nr,end=' ')

print()