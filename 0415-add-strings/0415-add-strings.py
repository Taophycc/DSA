class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n, m = len(num1) - 1, len(num2) - 1
        carry = 0
        ans = [] 

        while n >= 0 or m >= 0 or carry:
            digit1 = int(num1[n]) if n >= 0 else 0
            digit2 = int(num2[m]) if m >= 0 else 0
            
            total = digit1 + digit2 + carry
            
            carry = total // 10
            ans.append(str(total % 10))
            
            n -= 1
            m -= 1

        return "".join(ans[::-1])
