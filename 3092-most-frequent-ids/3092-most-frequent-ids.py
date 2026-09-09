class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        inventory = {}
        ans = []
        max_heap = []

        for i, num in enumerate(nums):
            if num in inventory:
                inventory[num] = inventory[num] + freq[i]
            else:
                inventory[num] = freq[i]

            heapq.heappush(max_heap, (-inventory[num], num))
            
            while max_heap and -max_heap[0][0] != inventory[max_heap[0][1]]:
                heapq.heappop(max_heap)
            ans.append(-max_heap[0][0])

        return ans

