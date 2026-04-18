class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            val = 0
            while x > 0:
                digit = x % 10
                val = val * 10 + digit
                x //= 10
            return val


        mp = {}
        dist = float('inf')

        for i, num in enumerate(nums):
            if num in mp:
                dist = min(dist, i - mp[num])
            mp[reverse(num)] = i

        if dist == float('inf'):
            return -1
        return dist