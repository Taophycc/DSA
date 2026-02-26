class Solution:
    def numSteps(self, s: str) -> int:
        carry = 0
        steps = 0

        for i in range(len(s) -1, 0, -1):
            digit = int(s[i])

            if digit + carry == 1:
                steps += 2
                carry = 1
            else:
                steps += 1
        return steps + carry