import random
import string


def random_mixed_string(length):
    ascii_chars = string.ascii_letters + string.digits
    combined_chars = ascii_chars
    result = ''.join(random.choices(combined_chars, k=length))
    return result


class Solution:
    def __init__(self, s):
        self.s = s

    def manacher(self):
        p = "^#" + "#".join(self.s) + "#$"
        m = len(p) // 2
        span = [0] * (m + 1)
        center, mid, right = 0, 0, 0
        i = 2
        while i <= m:
            j = 2 * mid - i
            span[i] = min(span[j], right - i) if i < right else 0
            while p[i - span[i] - 1] == p[i + span[i] + 1]:
                span[i] += 1
            if i + span[i] > right:
                mid = i
                right = i + span[i]
            if span[i] == i - 1:
                center = i
            i += 1
        return self.s[(center + span[center]) // 2:][::-1] + self.s

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
                j = next[j - 1]
        return self.s[next[-1]:][::-1] + self.s

    def shortest_palindrome(self):
        s1 = self.manacher()
        s2 = self.kmp_next()
        print("{:<10}".format("Manacher:"), s1)
        print("{:<10}".format("KMP:"), s2)
        assert s1 == s2, "Error"


if __name__ == '__main__':
    for i in range(100):
        length = random.randint(1, 10)
        s = random_mixed_string(length)
        print(s)
        sample = Solution(s)
        sample.shortest_palindrome()
