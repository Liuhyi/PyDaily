class Solution:
    def __init__(self, s: str):
        self.s = s

    def longest_prefix(self):
        m = len(self.s)
        next = [0] * m
        i = 1
        j = 0
        while i < m:
            if self.s[i] == self.s[j]:
                j += 1
                next[i] = j
                i += 1
            elif j == 0:
                next[i] = j
                i += 1
            else:
                j = next[j - 1]
        return self.s[:next[-1]]


if __name__ == '__main__':
    samples = ["ababab", "abababab", "ababababab", "abababababab", "ababababababab", "abababababababab",
              "ababababababababab","zsnddzsn", "zsnddzsnd", "zsnddzsndd", "zsnddzsnddz", "zsnddzsnddzs",
              "zsnddzsnddzsn", "zsnddzsnddzsnd", "zsnddzsnddzsndd", "zsnddzsnddzsnddz", "zsnddzsnddzsnddzs",
                "zsnddzsnddzsnddzsn", "zsnddzsnddzsnddzsnd", "zsnddzsnddzsnddzsndd", "zsnddzsnddzsnddzsnddz",]
    for sample in samples:
        s = Solution(sample)
        res = s.longest_prefix()
        res = res if res else "Empty"
        print(res)
