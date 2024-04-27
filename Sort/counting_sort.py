from base import Sorter


class CountingSorter(Sorter):
    def __init__(self, array):
        super().__init__(array)
        self.array = array[:]

    @Sorter.measure_time
    def sort(self):
        max_value = max(self.array)
        min_value = min(self.array)
        counting_array = [0] * (max_value - min_value + 1)
        for value in self.array:
            counting_array[value - min_value] += 1
        i = 0
        for j in range(len(counting_array)):
            while counting_array[j] > 0:
                self.array[i] = j + min_value
                i += 1
                counting_array[j] -= 1


if __name__ == '__main__':
    Sorter.test(CountingSorter, 1_000_000)