from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    # Initialize with 0:1 to handle subarrays starting from the very beginning
        cnt = Counter({0:1})
        ans = 0
        s = 0

        # Formula: CurrentPrefixSum - OldPrefixSum = Target(k)
        # Therefore: OldPrefixSum = CurrentPrefixSum - k
        
        for n in nums:
            # 1. Update Current Prefix Sum
            s += n 
            
            # 2. Check: Have we seen a prefix sum of (s - k) before?
            # If yes, it means the subarray between that old prefix and now sums to k.
            ans += cnt[s-k]
            
            # 3. Record the current prefix sum for future checks
            cnt[s] += 1
        
        return ans