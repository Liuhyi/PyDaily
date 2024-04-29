from base import Sorter


class RadixSorter(Sorter):
    def __init__(self, array):
        super().__init__(array)
        self.array = array[:]

    @Sorter.measure_time
    def sort(self):
        min_value = min(self.array)
        max_value = max(self.array)
        for (i, value) in enumerate(self.array):
            self.array[i] = value - min_value
        exp = 1
        while (max_value - min_value) // exp > 0:
            self._counting_sort(exp)
            exp *= 10
        for (i, value) in enumerate(self.array):
            self.array[i] = value + min_value

    def _counting_sort(self, exp):
        counting_array = [0] * 10
        output = [0] * len(self.array)
        for value in self.array:
            counting_array[(value // exp) % 10] += 1
        for i in range(1, 10):
            counting_array[i] += counting_array[i - 1]
        i = len(self.array) - 1
        while i >= 0:
            index = (self.array[i] // exp) % 10
            output[counting_array[index] - 1] = self.array[i]
            counting_array[index] -= 1
            i -= 1
        self.array = output


if __name__ == '__main__':
    Sorter.test(RadixSorter, 1_000_000)
