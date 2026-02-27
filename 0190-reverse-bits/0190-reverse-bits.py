class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # 1. Shift result left to make room for the incoming bit
            res <<= 1
            
            # 2. Extract the least significant bit of n and 'OR' it into the result
            res |= (n & 1)
            
            # 3. Shift n right to bring the next bit into the 'ones' position
            n >>= 1
        return res