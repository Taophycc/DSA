class Solution:
    def rotatedDigits(self, n: int) -> int:
        # in a range of 1 - n the good numbers are 2, 5, 6, 9 and invalid numbers are 3, 4, 7
        def isGood(num):
            hasGoodRotator = False
            while num > 0:
                digit = num % 10

                if digit == 3 or digit == 4 or digit == 7:
                    return False 
                if digit == 2 or digit == 5 or digit == 6 or digit == 9:
                    hasGoodRotator = True
                    
                num //= 10
            return hasGoodRotator

        cnt = 0
        for i in range(1, n+1):
            if isGood(i):
                cnt += 1
        return cnt
