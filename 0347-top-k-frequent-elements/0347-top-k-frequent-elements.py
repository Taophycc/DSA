from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        store = Counter(nums)
        
        min_heap = []
        for n, freq in store.items():
            heapq.heappush(min_heap, (freq, n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for freq, num in min_heap]