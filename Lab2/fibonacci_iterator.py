class Fibonacci:
    def __init__(self, steps):
        self.steps = steps
        self.index = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.steps:
            raise StopIteration
        self.index += 1
        fib_number = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib_number


fib = Fibonacci(10)
for num in fib:
    print(num)
