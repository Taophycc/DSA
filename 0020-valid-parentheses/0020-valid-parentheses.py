class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openAndClose = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in openAndClose:
                if stack and stack[-1] == openAndClose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        return not stack