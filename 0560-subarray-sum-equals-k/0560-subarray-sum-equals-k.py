class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0

        prefix_map = {0:1}
        curr_sum = 0

        for num in nums:
            curr_sum += num
            target = curr_sum - k
            
            if target in prefix_map:
                cnt+= prefix_map[target]

            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1
        return cnt
