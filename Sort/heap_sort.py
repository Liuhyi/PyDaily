from base import Sorter


class HeapSorter(Sorter):
    def __init__(self, array):
        super().__init__(array)
        self.array = array[:]

    def _heapify(self, n, i):
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.array[i] < self.array[left]:
                largest = left
            if right < n and self.array[largest] < self.array[right]:
                largest = right
            if largest == i:
                break
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            i = largest

    def _heap_sort(self):
        n = len(self.array)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self._heapify(i, 0)

    @Sorter.measure_time
    def sort(self):
        self._heap_sort()


if __name__ == '__main__':
    Sorter.test(HeapSorter, 1_000_000)

