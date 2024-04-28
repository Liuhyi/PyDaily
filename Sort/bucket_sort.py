from base import Sorter


class BucketSorter(Sorter):
    def __init__(self, array):
        super().__init__(array)
        self.array = array[:]

    @Sorter.measure_time
    def sort(self):
        max_value = max(self.array)
        min_value = min(self.array)
        bucket_size = 10
        bucket_count = (max_value - min_value) // bucket_size + 1
        buckets = [[] for _ in range(bucket_count)]
        for value in self.array:
            buckets[(value - min_value) // bucket_size].append(value)
        i = 0
        for bucket in buckets:
            bucket.sort()
            for value in bucket:
                self.array[i] = value
                i += 1


if __name__ == '__main__':
    Sorter.test(BucketSorter, 1_000_000)
