import random

from Sort import sorters


def test(count=100_000):
    nums = [random.randint(-count, count) for _ in range(count)]
    for sorter in sorters:
        sorter(nums).sort()


if __name__ == '__main__':
    test()
