class Solution:
    def __init__(self, s: str, sub: str):
        self.s = s
        self.sub = sub

    def get_next(self):
        next = [-1] * len(self.sub)
        i = 0
        j = -1
        while i < len(self.sub) - 1:
            if j == -1 or self.sub[i] == self.sub[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
        return next

    def get_index(self):
        next = self.get_next()
        i = 0
        j = 0
        while i < len(self.s) and j < len(self.sub):
            if j == -1 or self.s[i] == self.sub[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(self.sub):
            return i - j
        else:
            return -1


if __name__ == '__main__':
    samples = [("hello", "ll"), ("aaaaa", "bba"), ("mississippi", "issip"), ("a", "a"), ("a", "b"),
               ("a", ""), ("", "a"), ("", ""), ("a", "aa"), ("aa", "a"), ("aa", "aa"), ("aa", "aaa"),
               ("aaa", "aa"), ("aaa", "aaa"), ("hello", ""), ("", "hello"), ("hello", "hello"),
               ("hello", "world"), ("world", "hello"), ("world", "world"), ("world", ""), ("", "world"),
               ("hello", "o"), ("hello", "lo"), ("hello", "ll"), ("hello", "ell"), ("hello", "hello"),
               ("hello", "h"), ("hello", "he"), ("hello", "hel"), ("hello", "hell"), ("hello", "hello"),
               ("hello", "e"), ("hello", "el"), ("hello", "ell"), ("hello", "ello"), ("hello", "hello"),
               ("hello", "l"), ("hello", "ll"), ("hello", "llo"), ("hello", "llo"), ("hello", "hello"),
               ("hello", "o"), ("hello", "lo"), ("hello", "llo"), ("hello", "llo"), ("hello", "hello")]
    for sample in samples:
        s = Solution(sample[0], sample[1])
        print(s.get_index())
