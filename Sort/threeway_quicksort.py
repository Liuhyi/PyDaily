import random
from base import Sorter


class ThreeWaySorter(Sorter):
    def __init__(self, array):
        # Create independent copies of the number array for different sorting methods.
        super().__init__(array)
        self.array = array[:]

    def _three_way_quicksort(self, low, high):
        """Recursively sort the array using the three-way quicksort algorithm."""
        if low >= high:
            return

        lt, gt, i = low, high, low
        pivot = self.array[random.randint(low, high)]

        while i <= gt:
            if self.array[i] < pivot:
                self.array[lt], self.array[i] = self.array[i], self.array[
                    lt]
                lt += 1
                i += 1
            elif self.array[i] > pivot:
                self.array[gt], self.array[i] = self.array[i], self.array[
                    gt]
                gt -= 1
            else:
                i += 1

        self._three_way_quicksort(low, lt - 1)
        self._three_way_quicksort(gt + 1, high)

    @Sorter.measure_time
    def sort(self):
        """Sort using the three-way quicksort algorithm."""
        self._three_way_quicksort(0, len(self.array) - 1)


if __name__ == '__main__':
    Sorter.test(ThreeWaySorter, 1_000_000)
