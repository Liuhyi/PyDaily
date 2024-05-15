import random
import time


class StringMultiplier:
    def __init__(self, num1, num2):
        self.num1 = num1.lstrip("0")
        self.num2 = num2.lstrip("0")

    @staticmethod
    def measure_time(func):
        def timed(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Function {func.__qualname__.split('.')[-1]:<20} takes  {end_time - start_time:.40f} seconds.")
            return result

        return timed

    @measure_time
    def multiply(self) -> str:
        if self.num1 == "" or self.num2 == "":
            return "0"
        m, n = len(self.num1), len(self.num2)
        res = [0] * (m + n)
        lst1 = [int(i) for i in self.num1]
        lst2 = [int(i) for i in self.num2]
        for i in range(m - 1, -1, -1):
            carry = 0
            for j in range(n - 1, -1, -1):
                carry, res[i + j + 1] = divmod(lst1[i] * lst2[j] + carry + res[i + j + 1], 10)
            res[i] = carry
        l = 0
        if res[0] == 0:
            l += 1
        return "".join(str(i) for i in res[l:])

    @measure_time
    def built_in_multiply(self) -> str:
        return str(int(self.num1) * int(self.num2))

    def test(self):
        custom = self.multiply()
        builtin = self.built_in_multiply()
        print("{:<30}".format("StringMultiplication:"), custom)
        print("{:<30}".format("Built-inMultiplication:"), builtin)
        assert custom == builtin, "Error"


if __name__ == '__main__':
    counts = 100
    digits = 2000
    for i in range(counts):
        num1 = "".join([str(random.randint(0, 9)) for _ in range(digits)])
        num2 = "".join([str(random.randint(0, 9)) for _ in range(digits)])
        sample = StringMultiplier(num1, num2)
        sample.test()

