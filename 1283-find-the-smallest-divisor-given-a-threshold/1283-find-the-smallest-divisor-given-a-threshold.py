class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low, high = 1, max(nums)
        res = 0

        while low <= high:
            total_box = 0
            mid = (low+high) // 2
            k = mid
            
            for num in nums:
                total_box += math.ceil(num/k)
            
            if total_box <= threshold:
                res = mid
                high = mid -1
            else:
                low = mid + 1
        return res
