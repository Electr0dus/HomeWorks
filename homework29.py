class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        if self.start >= self.end:
            raise Exception(f'Значения start {self.start} должно быть меньше end {self.end}')

    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        if self.i == self.end:
            raise StopIteration()
        if self.i % 2 == 0:
            self.i += 1
            return self.i - 1
        else:
            self.i += 1


en = EvenNumbers(10, 25)
for i in en:
    if isinstance(i, int):
        print(i)
