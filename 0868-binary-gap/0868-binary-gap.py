class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        stack = []
        while n > 0:
            temp = n & 1
            n = n >> 1
            if not stack:
                if temp == 1:
                    stack.append(temp)
            else:
                if temp == 0:
                    stack.append(temp)
                else:
                    ans = max(ans, len(stack))
                    stack = [temp]
        return ans

