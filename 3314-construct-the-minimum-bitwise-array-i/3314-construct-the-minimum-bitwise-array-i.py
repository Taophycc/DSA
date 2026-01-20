class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        ans = []
      
        for num in nums:
            if num == 2:
                ans.append(-1)
            else:
                for bit_position in range(1, 32):
                    if ((num >> bit_position) & 1) == 0:
                        answer = num ^ (1 << (bit_position - 1))
                        ans.append(answer)
                        break

        return ans