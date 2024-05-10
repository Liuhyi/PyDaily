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
    samples = ["abc", "aaa", "abba", "ababa", "abbaa", "ababaa", "ababba", "ababbba", "ababab", "abababa",
                "abababba", "ababababa", "ababababba", "abababababa", "abababababba", "ababababababa",
                "ababababababba", "abababababababa", "abababababababba", "ababababababababa", "ababababababababba",
                "abababababababababa", "abababababababababba", "ababababababababababa",]
    for sample in samples:
        s = Solution(sample)
        print(s.countSubstrings())
