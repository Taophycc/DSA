class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low, high = 1 , max(piles)
        res = 0

        while low <= high:
            p = 0
            mid = (low+high)//2
            k = mid
            for pile in piles:
                p += (pile + k - 1) // k
                # p += math.ceil(pile//k)

            if p <= h: 
                res = k
                high = mid -1
            else:
                low = mid + 1
        return res
