from base import Sorter


class BubbleSorter(Sorter):
    def __init__(self, array):
        super().__init__(array)
        self.array = array[:]

    @Sorter.measure_time
    def sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]


if __name__ == '__main__':
    Sorter.test(BubbleSorter, 1_000_0)

