class Solution:
    def numSteps(self, s: str) -> int:
        # 1101 - 13
        # if odd didvide by 2
        cnt = 0
        num = int(s, 2)
        while num != 1:
            if num & 1:
                num += 1
            else:
                num//=2
            cnt += 1
        return cnt
