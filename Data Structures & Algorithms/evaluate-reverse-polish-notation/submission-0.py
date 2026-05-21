class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(float(a) / b),
        }

        for c in tokens:
            if c in operations:
                a, b = stack.pop(), stack.pop()
                stack.append(operations[c](b, a))  # note b, a order for subtraction/division
            else:
                stack.append(int(c))

        return stack[0]