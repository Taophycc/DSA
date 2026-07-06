class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                char_string = ""
                while stack and stack[-1] != "[":
                    char_string = stack.pop() + char_string
                stack.pop()

                num_string = ""
                while stack and stack[-1].isdigit():
                    num_string = stack.pop() + num_string
                n = int(num_string)
                stack.append(char_string*n)
        
        return "".join(stack)