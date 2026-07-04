class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n = len(nums)
        mini = min(nums)
        maxi = max(nums)
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        return gcd(mini, maxi)