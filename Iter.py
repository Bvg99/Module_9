class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.current = self.start if self.start % 2 == 0 else self.start + 1


    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            printed_number = self.current
            self.current += + 2
            return printed_number
        raise StopIteration

en = EvenNumbers(10, 25)
for i in en:
    print(i)