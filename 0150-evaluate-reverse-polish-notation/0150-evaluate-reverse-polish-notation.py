class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c in "+-*/":
                a = stack.pop()
                b = stack.pop()

                match c:
                    case '+':
                        result = b + a
                    case '-':
                        result = b - a
                    case '*':
                        result = b * a
                    case '/':
                        result = int(b / a)
                stack.append(result)
            else:
                stack.append(int(c))
            
        return stack.pop()