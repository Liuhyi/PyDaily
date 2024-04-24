import random
from base import Sorter


class LomutoSorter(Sorter):
    def __init__(self, array):
        # Create independent copies of the number array for different sorting methods.
        super().__init__(array)
        self.array = array[:]

    def _lomuto_quicksort(self, low, high):
        """Recursively sort the array using the lomuto quicksort algorithm."""
        if low >= high:
            return

        pivot_index = random.randint(low, high)
        pivot = self.array[pivot_index]
        self.array[high], self.array[pivot_index] = pivot, self.array[high]
        lt = low
        for i in range(low, high):
            if self.array[i] < pivot:
                self.array[i], self.array[lt] = self.array[lt], self.array[i]
                lt += 1
        self.array[lt], self.array[high] = self.array[high], self.array[lt]
        self._lomuto_quicksort(low, lt - 1)
        self._lomuto_quicksort(lt + 1, high)

    @Sorter.measure_time
    def sort(self):
        self._lomuto_quicksort(0, len(self.array) - 1)


if __name__ == '__main__':
    Sorter.test(LomutoSorter, 1_000_000)
