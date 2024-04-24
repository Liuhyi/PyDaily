import random
from base import Sorter


class HoareSorter(Sorter):
    def __init__(self, array):
        # Create independent copies of the number array for different sorting methods.
        super().__init__(array)
        self.array = array[:]

    def _hoare_quicksort(self, low, high):
        if low >= high:
            return
        pivot_index = random.randint(low, high)
        pivot = self.array[pivot_index]
        self.array[low], self.array[pivot_index] = self.array[pivot_index], self.array[low]
        i = low + 1
        j = high
        while True:
            while i <= j and self.array[i] <= pivot:
                i += 1
            while i <= j and self.array[j] >= pivot:
                j -= 1
            if i <= j:
                self.array[i], self.array[j] = self.array[j], self.array[i]
            else:
                break

        self.array[low], self.array[j] = self.array[j], self.array[low]
        self._hoare_quicksort(low, j - 1)
        self._hoare_quicksort(j + 1, high)

    @Sorter.measure_time
    def sort(self):
        self._hoare_quicksort(0, len(self.array) - 1)


if __name__ == '__main__':
    Sorter.test(HoareSorter,1_000)
