import time


class Sorter:
    def __init__(self, array):
        self.builtin_sort_array = array

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

    @measure_time
    def builtin_sort(self):
        """Sort using Python’s built-in sort method."""
        self.builtin_sort_array.sort()

    def sort(self):
        raise "Sort not implemented yet"
        pass
