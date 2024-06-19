class Calculator:
    def calculate(self, s: str) -> int:
        def update(op, val):
            if op == '+':
                stack.append(val)
            elif op == '-':
                stack.append(-val)
            elif op == '*':
                stack.append(stack.pop() * val)
            elif op == '/':
                stack.append(stack.pop() / val)  # 使用int()来处理负数除法

        i, n = 0, len(s)
        stack = []
        num = 0
        sign = '+'

        while i < n:
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in '+-*/':
                update(sign, num)
                num, sign = 0, s[i]
            elif s[i] == '(':
                stack.append(sign)
                stack.append('(')
                num, sign = 0, '+'
            elif s[i] == ')':
                update(sign, num)
                num = 0
                while stack[-1] != '(':
                    num += stack.pop()
                stack.pop()
                sign = stack.pop()
                update(sign, num)
                num = 0
            i += 1

        if num != 0:
            update(sign, num)

        return sum(stack)


if __name__ == '__main__':
    s = "(1+(4+5+2)-3)+(6+845) + 23 * 123 / 12 + 123"
    calculator = Calculator()
    my_result = calculator.calculate(s)
    print(f"My result: {my_result}")
    correct_result = eval(s)
    print(f"Correct result: {correct_result}")
    assert eval(s) == calculator.calculate(s), "Error"
