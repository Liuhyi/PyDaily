import time
import random


class Sorter:
    def __init__(self, array):
        self.builtin_array = array[:]

    @staticmethod
    def measure_time(func):
        """Decorator to measure the execution time of a function."""

        def timed(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Function '{func.__qualname__}' takes  {end_time - start_time:.6f} seconds.")
            return result

        return timed

    @measure_time
    def sort(self):
        if self.__class__.__name__ != "Sorter":
            raise NotImplementedError("This method should be implemented in the derived class.")
        self.builtin_array.sort()

    @measure_time
    def built_in_sort(self):
        self.builtin_array.sort()

    @staticmethod
    def test(arraySorter, count=1_000_000):
        nums = [random.randint(-count, count) for _ in range(count)]
        sorter = arraySorter(nums)
        sorter.sort()
        sorter.built_in_sort()
        assert sorter.builtin_array == sorter.array, "The array is not sorted correctly."
