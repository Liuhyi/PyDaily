from base import Sorter


class MergeSorter(Sorter):
    def __init__(self, array):
        super().__init__(array)
        self.array = array[:]

    def _merge(self, low, mid, high):
        left = self.array[low:mid + 1]
        right = self.array[mid + 1:high + 1]
        left.append(float('inf'))
        right.append(float('inf'))
        i = j = 0
        for k in range(low, high + 1):
            if left[i] <= right[j]:
                self.array[k] = left[i]
                i += 1
            else:
                self.array[k] = right[j]
                j += 1

    def _merge_sort(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self._merge_sort(low, mid)
            self._merge_sort(mid + 1, high)
            self._merge(low, mid, high)

    @Sorter.measure_time
    def sort(self):
        self._merge_sort(0, len(self.array) - 1)


if __name__ == '__main__':
    Sorter.test(MergeSorter, 1_000_000)
