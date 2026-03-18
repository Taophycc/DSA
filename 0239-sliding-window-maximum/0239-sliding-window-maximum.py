import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []

        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            if i >= k-1:
                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)
                res.append(-max_heap[0][0])
        return res