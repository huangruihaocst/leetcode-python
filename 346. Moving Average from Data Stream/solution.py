class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.window = list()
        self.pointer = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.window) < self.size:
            self.window.append(val)
        else:
            self.window[self.pointer] = val
            self.pointer = (self.pointer + 1) % self.size
        return sum(self.window) / len(self.window)


if __name__ == '__main__':
    m = MovingAverage(3)
    print(m.next(1))
    print(m.next(10))
    print(m.next(3))
    print(m.next(5))
