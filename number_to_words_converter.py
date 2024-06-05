import random


class Solution:
    def __init__(self):
        self.map = [
            ["", "", ""],
            ["One", "Ten", "One Hundred"],
            ["Two", "Twenty", "Two Hundred"],
            ["Three", "Thirty", "Three Hundred"],
            ["Four", "Forty", "Four Hundred"],
            ["Five", "Fifty", "Five Hundred"],
            ["Six", "Sixty", "Six Hundred"],
            ["Seven", "Seventy", "Seven Hundred"],
            ["Eight", "Eighty", "Eight Hundred"],
            ["Nine", "Ninety", "Nine Hundred"]
        ]
        self.steps = ["", "Thousand", "Million", "Billion"]
        self.teens = [
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

    def number_to_words(self, num: int) -> str:
        res = []
        i = 0
        while num > 0:
            cur = num % 1000
            num //= 1000
            if cur > 0:
                res.append((self.convert_three_digits(cur) + " " + self.steps[i]).strip())
            i += 1
        return ' '.join(res[::-1])

    def convert_three_digits(self, num: int) -> str:
        result = []
        hundred, num = divmod(num, 100)
        if hundred > 0:
            result.append(self.map[hundred][2])
        if num > 0:
            if num < 10:
                result.append(self.map[num][0])
            elif num < 20:
                result.append(self.teens[num - 10])
            else:
                result.append(self.map[num // 10][1])
                if num % 10 > 0:
                    result.append(self.map[num % 10][0])
        return ' '.join(result)


if __name__ == '__main__':
    sample_counts = 100
    for i in range(sample_counts):
        num = random.randint(1, 2**31 - 1)
        print(num, Solution().number_to_words(num))

