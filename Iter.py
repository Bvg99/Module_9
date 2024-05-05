class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == 0:
            print(self.start)
        self.i += 1
        if self.start % 2 != 0:
            self.start = self.start + 1
        self.start = self.start + 2
        if self.start > self.end:
            raise StopIteration
        return self.start


en = EvenNumbers(10, 25)
for i in en:
    print(i)