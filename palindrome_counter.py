import random


class Solution:
    def __init__(self, s: str):
        self.s = s

    def countSubstrings(self) -> int:
        p = "^#" + "#".join(self.s) + "#$"
        check = [0] * len(p)
        right = 0
        mid = 0
        res = 0
        for i in range(1, len(p) - 1):
            j = 2 * mid - i
            check[i] = min(check[j], right - i) if i < right else 0
            while p[i - check[i] - 1] == p[i + check[i] + 1]:
                check[i] += 1
            if i + check[i] > right:
                mid = i
                right = i + check[i]
            res += (check[i] + 1) // 2
        return res


if __name__ == '__main__':
    numbers = 100
    length = 4
    samples = ["".join(random.choices("abc", k=length)) for _ in range(numbers)]
    for sample in samples:
        s = Solution(sample)
        print("{:<{}}".format(sample + ":", length + 2), s.countSubstrings())
