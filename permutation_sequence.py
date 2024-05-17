class Solution:

    def __init__(self, n, k):
        self.n = n
        self.k = k

    def getPermutation(self) -> str:
        self.k -= 1
        factorials = 1
        for i in range(1, self.n + 1):
            factorials *= i
        digits = [str(i) for i in range(1, self.n + 1)]
        res = [0] * self.n
        for i in range(self.n):
            factorials //= self.n - i
            index, self.k = divmod(self.k, factorials)
            res[i] = digits[index]
            digits.pop(index)
        return "".join(res)

    def test(self):
        print("n = ", self.n, "k = ", self.k, "Permutation = ", self.getPermutation())


if __name__ == '__main__':
    samples = [(3, 3), (4, 9), (9, 100), (9, 1000),(9, 10000), (9, 100000)]
    for sample in samples:
        s = Solution(sample[0], sample[1])
        s.test()
