class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        #13 13 % 10 4 remainder 1
        #4 4 % 10 0 rem 4 
        def getD(num):
            arr = []
            while num > 0:
                digit = num % 10
                arr.append(digit)
                num//=10
            return arr[::-1]
        res = []
        for num in nums:
            res.extend(getD(num))
        return res