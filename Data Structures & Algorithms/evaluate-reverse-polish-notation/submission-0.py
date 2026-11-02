class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operators:
                second, first = int(stack.pop()), int(stack.pop())

                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:
                    stack.append(first / second)
            else:
                stack.append(token)
        
        return int(stack.pop())