import random
import sys
from Sort.quicksort import Sorter


class ArraySorter(Sorter):
    def __init__(self, numbers):
        # Create independent copies of the number array for different sorting methods.
        super().__init__(numbers)
        self.lomuto_array = numbers[:]

    def _lomuto_quicksort(self, low, high):
        """Recursively sort the array using the lomuto quicksort algorithm."""
        if low >= high:
            return

        pivot_index = random.randint(low, high)
        pivot = self.lomuto_array[pivot_index]
        self.lomuto_array[high], self.lomuto_array[pivot_index] = pivot, self.lomuto_array[high]
        lt = low
        for i in range(low, high):
            if self.lomuto_array[i] < pivot:
                self.lomuto_array[i], self.lomuto_array[lt] = self.lomuto_array[lt], self.lomuto_array[i]
                lt += 1
        self.lomuto_array[lt], self.lomuto_array[high] = self.lomuto_array[high], self.lomuto_array[lt]
        self._lomuto_quicksort(low, lt - 1)
        self._lomuto_quicksort(lt + 1, high)

    @Sorter.measure_time
    def sort(self):
        """Sort using the three-way quicksort algorithm."""
        self._lomuto_quicksort(0, len(self.lomuto_array) - 1)


if __name__ == '__main__':
    print(sys.path)
    number_count = 10_000
    numbers = [random.randint(0, number_count) for _ in range(number_count)]
    sorter = ArraySorter(numbers)
    sorter.sort()
    sorter.builtin_sort()
    assert sorter.lomuto_array == sorter.builtin_sort_array, "Arrays do not match after sorting."
