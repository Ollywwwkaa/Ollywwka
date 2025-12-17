class Frange:
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            start, stop = 0, start
        if step is None:
            step = 1.0
        self.start = float(start)
        self.stop = float(stop)
        self.step = float(step)
        self.current = self.start
    def __iter__(self):
        self.current = self.start
        return self
    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        value = self.current
        self.current += self.step
        return value
for x in Frange(1, 3, 0.5):
    print(x)
for x in Frange(5, 1, -0.5):
    print(x)
for x in Frange(3):
    print(x)
for x in Frange(1.2, 3.2):
    print(x)
