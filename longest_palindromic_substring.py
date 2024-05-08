class Solution:
    def longest_Palindrome(self, s: str) -> str:
        p = "^#" + "#".join(s) + "#$"
        check = [0] * len(p)
        right = 0
        mid = 0
        max_length = 0
        index = 0
        for i in range(1, len(p) - 1):
            j = 2 * mid - i
            check[i] = min(check[j], right - i) if i < right else 0
            while p[i - check[i] - 1] == p[i + check[i] + 1]:
                check[i] += 1
            if i + check[i] > right:
                mid = i
                right = i + check[i]
            if check[i] > max_length:
                max_length = check[i]
                index = i
        start = (index - max_length) // 2
        end = start + max_length
        return s[start:end]


if __name__ == '__main__':
    s = Solution()
    print(s.longest_Palindrome("babad"))
    print(s.longest_Palindrome("cbbd"))
    print(s.longest_Palindrome("a"))
    print(s.longest_Palindrome("ac"))
    print(s.longest_Palindrome("bb"))
    print(s.longest_Palindrome("ccc"))
    print(s.longest_Palindrome("aaaa"))
    print(s.longest_Palindrome("ab"))
    print(s.longest_Palindrome("abc"))
    print(s.longest_Palindrome("abbc"))
    print(s.longest_Palindrome("abcc"))
    print(s.longest_Palindrome("abbc"))
    print(s.longest_Palindrome("abbcc"))
    print(s.longest_Palindrome("abbccc"))
    print(s.longest_Palindrome("abbcccc"))
    print(s.longest_Palindrome("abbccccc"))
    print(s.longest_Palindrome("abbcccccc"))
    print(s.longest_Palindrome("abbccccccc"))
    print(s.longest_Palindrome("abbcccccccc"))
    print(s.longest_Palindrome("abbccccccccc"))
    print(s.longest_Palindrome("abbcccccccccc"))
    print(s.longest_Palindrome("abbccccccccccc"))
    print(s.longest_Palindrome("abbcccccccccccc"))
    print(s.longest_Palindrome("abbccccccccccccc"))
    print(s.longest_Palindrome("abbcccccccccccccc"))
    print(s.longest_Palindrome("abbccccccccccccccc"))
    print(s.longest_Palindrome("abbcccccccccccccccc"))
    print(s.longest_Palindrome("abbccccccccccccccccc"))
    print(s.longest_Palindrome("abbcccccccccccccccccc"))
    print(s.longest_Palindrome("abbccccccccccccccccccc"))
    print(s.longest_Palindrome("abbcccccccccccccccccccc"))
    print(s.longest_Palindrome("abbccccccccccccccccccccc"))
    print(s.longest_Palindrome("abbcccccccccccccccccccccc"))
    print(s.longest_Palindrome("abbccccccccccccccccccccccc"))
    print(s.longest_Palindrome("abbcccccccccccccccccccccccc"))
    print(s.longest_Palindrome("abbccccccccccccccccccccccccc"))
