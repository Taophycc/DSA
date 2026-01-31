from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = Counter({0:1})
        ans = 0
        s = 0

        for n in nums:
            s += n
            ans += cnt[s-k]
            cnt[s] += 1
        return ans