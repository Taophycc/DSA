class Solution:
    def decodeString(self, s: str) -> str:
        # keep pushing until i get to a "]" -> stack = 3
        # check the top of that stack and pop the values while creating a substring till we get "[" and then pop it
        # then top of the stack becomes the digit we then multiply that woth the substring
        # keep going until you hit a “]“ pop the top till the top becomes "[" -> 
        stack = []
        ans = ""
        n = len(s)

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                # pop the "["    
                stack.pop()
                
                # deal with numbers. edge case it could be multi digit
                numstring = ""
                while stack and stack[-1].isdigit():
                    numstring = stack.pop() + numstring
                n = int(numstring)
            
                stack.append(n*substring)

        return "".join(stack)