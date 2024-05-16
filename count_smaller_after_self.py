import random


class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.res = [0] * len(nums)
        self.indices = list(range(len(nums)))

    def countSmaller(self):
        self.merge_sort(0, len(self.nums) - 1)
        return self.res

    def merge_sort(self, left, right):
        if left >= right:
            return

        mid = left + (right - left) // 2
        self.merge_sort(left, mid)
        self.merge_sort(mid + 1, right)
        self.merge(left, mid, right)

    def merge(self, left, mid, right):
        left_part = self.indices[left:mid + 1]
        right_part = self.indices[mid + 1:right + 1]

        i, j = 0, 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if self.nums[left_part[i]] > self.nums[right_part[j]]:
                self.indices[k] = left_part[i]
                self.res[left_part[i]] += len(right_part) - j
                i += 1
            else:
                self.indices[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            self.indices[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            self.indices[k] = right_part[j]
            j += 1
            k += 1

    def run(self):
        print(self.nums, self.countSmaller())


if __name__ == '__main__':
    counts = 100
    length = 5
    for i in range(counts):
        nums = [random.randint(1, 100) for _ in range(length)]
        sample = Solution(nums)
        sample.run()

