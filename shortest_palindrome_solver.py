
class Solution:
    def __init__(self,s):
        self.s = s

    def manacher(self):
        p = "^#" + "#".join(self.s) + "#$"
        m = len(p) // 2
        span = [0] * (m+1)
        center, mid, right = 0, 0, 0
        i = 2
        while i <= m:
            j = 2 * mid - i
            span[i] = min(span[j],right - i) if i < right else 0
            while p[i-span[i]-1] == p[i+span[i]+1]:
                span[i] += 1
            if i + span[i] > right:
                mid = i
                right = i + span[i]
            if span[i] == i - 1:
                center = i
            i += 1
        return self.s[(center+span[center]) // 2:][::-1] + self.s

    def kmp_next(self):
        rev = self.s[::-1]
        p = self.s + "#" + rev
        next = len(p) * [0]
        i, j = 1, 0
        while i < len(p):
            if p[i] == p[j]:
                j += 1
                next[i] = j
                i += 1
            elif j == 0:
                next[i] = j
                i += 1
            else:
                j = next[j-1]
        return self.s[next[-1]:][::-1] + self.s

    def shortest_palindrome(self):
        s1 = self.manacher()
        s2 = self.kmp_next()
        print("Manacher:", s1)
        print("KMP:", s2)
        assert s1 == s2, "Error"


if __name__ == '__main__':
    samples = ["aacecaaa", "abcd", "a", "aa", "ab", "aba", "abac", "abacd", "abacde", "abacdef", "abacdefg",
               "abacdefgh", "abacdefghi", "abacdefghij", "abacdefghijk", "abacdefghijkl", "abacdefghijklm",
               "abacdefghijklmn", "abacdefghijklmno", "abacdefghijklmnop", "abacdefghijklmnopq", "abacdefghijklmnopqr",
               "abacdefghijklmnopqrs", "abacdefghijklmnopqrst", "abacdefghijklmnopqrstu", "abacdefghijklmnopqrstuv",
               "abacdefghijklmnopqrstuvw", "abacdefghijklmnopqrstuvwx", "abacdefghijklmnopqrstuvwxy",
               "abacdefghijklmnopqrstuvwxyz", "abacdefghijklmnopqrstuvwxyzA", "abacdefghijklmnopqrstuvwxyzAB",
               "abacdefghijklmnopqrstuvwxyzABC", "abacdefghijklmnopqrstuvwxyzABCD", "abacdefghijklmnopqrstuvwxyzABCDE",
               "abacdefghijklmnopqrstuvwxyzABCDEF", "abacdefghijklmnopqrstuvwxyzABCDEFG", "abacdefghijklmnopqrstuvwxyzABCDEFGH",
               "abacdefghijklmnopqrstuvwxyzABCDEFGHI", "abacdefghijklmnopqrstuvwxyzABCDEFGHIJ", "abacdefghijklmnopqrstuvwxyzABCDEFGHIJK",
               "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKL", "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLM", "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN",
               "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO", "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP", "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ",
               "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR", "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS", "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST",
               "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU", "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV", "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW",
               "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX", "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYY", "abacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYX"]
    for sample in samples:
        s = Solution(sample)
        s.shortest_palindrome()


