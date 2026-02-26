class Solution:
    def numSteps(self, s: str) -> int:
        cnt = 0
        num = int(s, 2)
        while num != 1:
            if num & 1:
                num += 1
            else:
                num >>= 1
            cnt += 1
        return cnt
