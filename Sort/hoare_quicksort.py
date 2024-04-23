import random
from base import Sorter


class ArraySorter(Sorter):
    def __init__(self, array):
        # Create independent copies of the number array for different sorting methods.
        super().__init__(array)
        self.hoare_array = array[:]

    def _hoare_quicksort(self, low, high):
        if low >= high:
            return
        pivot_index = random.randint(low, high)
        pivot = self.hoare_array[pivot_index]
        self.hoare_array[low], self.hoare_array[pivot_index] = self.hoare_array[pivot_index], self.hoare_array[low]
        i = low + 1
        j = high
        while True:
            while i <= j and self.hoare_array[i] <= pivot:
                i += 1
            while i <= j and self.hoare_array[j] >= pivot:
                j -= 1
            if i <= j:
                self.hoare_array[i], self.hoare_array[j] = self.hoare_array[j], self.hoare_array[i]
            else:
                break

        self.hoare_array[low], self.hoare_array[j] = self.hoare_array[j], self.hoare_array[low]
        self._hoare_quicksort(low, j - 1)
        self._hoare_quicksort(j + 1, high)

    @Sorter.measure_time
    def sort(self):
        self._hoare_quicksort(0, len(self.hoare_array) - 1)


if __name__ == '__main__':
    number_count = 10_000_000
    numbers = [random.randint(0, number_count) for _ in range(number_count)]
    sorter = ArraySorter(numbers)
    sorter.sort()
    sorter.builtin_sort()
    assert sorter.hoare_array == sorter.builtin_sort_array, "Arrays do not match after sorting."
