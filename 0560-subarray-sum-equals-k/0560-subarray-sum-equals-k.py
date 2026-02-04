from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize with 0:1 to handle subarrays starting from the very beginning
        cnt = Counter({0:1})
        ans = 0
        s = 0

        for num in nums:
            s += num

            ans += cnt[s-k]

            cnt[s] += 1
        
        return ans