import random


class Counter:
    def count(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return sum(is_prime)


if __name__ == '__main__':
    samples_count = 10
    c = Counter()
    for i in range(samples_count):
        n = random.randint(1, 100)
        print("the number of prime numbers that are less than", n, "is", c.count(n))
