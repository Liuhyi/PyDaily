from typing_extensions import List


class Solution:
    def evaluate(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    stack.append(int(left / right))
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == '__main__':
    tokens = ["2", "1", "+", "3", "*"]
    s = Solution()
    print(s.evaluate(tokens))
    tokens = ["4", "13", "5", "/", "+"]
    print(s.evaluate(tokens))
