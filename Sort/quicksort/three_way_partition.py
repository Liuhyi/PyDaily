import random
import time


class ArraySorter:
    def __init__(self, numbers):
        # Create independent copies of the number array for different sorting methods.
        self.quick_sort_array = numbers[:]
        self.builtin_sort_array = numbers[:]

    @staticmethod
    def measure_time(func):
        """Decorator to measure the execution time of a function."""

        def timed(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds.")
            return result

        return timed

    def _three_way_quicksort(self, low, high):
        """Recursively sort the array using the three-way quicksort algorithm."""
        if low >= high:
            return

        lt, gt, i = low, high, low
        pivot = self.quick_sort_array[random.randint(low, high)]

        while i <= gt:
            if self.quick_sort_array[i] < pivot:
                self.quick_sort_array[lt], self.quick_sort_array[i] = self.quick_sort_array[i], self.quick_sort_array[lt]
                lt += 1
                i += 1
            elif self.quick_sort_array[i] > pivot:
                self.quick_sort_array[gt], self.quick_sort_array[i] = self.quick_sort_array[i], self.quick_sort_array[gt]
                gt -= 1
            else:
                i += 1

        self._three_way_quicksort(low, lt - 1)
        self._three_way_quicksort(gt + 1, high)

    @measure_time
    def quicksort(self):
        """Sort using the three-way quicksort algorithm."""
        self._three_way_quicksort(0, len(self.quick_sort_array) - 1)

    @measure_time
    def builtin_sort(self):
        """Sort using Python’s built-in sort method."""
        self.builtin_sort_array.sort()


if __name__ == '__main__':
    number_count = 10_000_000
    numbers = [random.randint(0, number_count) for _ in range(number_count)]
    sorter = ArraySorter(numbers)
    sorter.quicksort()
    sorter.builtin_sort()
    assert sorter.quick_sort_array == sorter.builtin_sort_array, "Arrays do not match after sorting."

