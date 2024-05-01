from base import Sorter


class ShellSorter(Sorter):
    def __init__(self, array):
        super().__init__(array)
        self.array = array[:]

    @Sorter.measure_time
    def sort(self):
        n = len(self.array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.array[i]
                j = i
                while j >= gap and self.array[j - gap] > temp:
                    self.array[j] = self.array[j - gap]
                    j -= gap
                self.array[j] = temp
            gap //= 2


if __name__ == '__main__':
    Sorter.test(ShellSorter, 1_000_000)