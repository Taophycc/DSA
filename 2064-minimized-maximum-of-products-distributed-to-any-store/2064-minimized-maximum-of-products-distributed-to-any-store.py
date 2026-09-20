class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        low, high = 1 , max(quantities)
        res = 0

        while low <= high:
            mid = (low + high) // 2
            x = mid
            total_stores = 0

            for  q in quantities:
                total_stores += (q + x - 1) // x
            
            if total_stores <= n:
                res = x
                high = mid - 1
            else:
                low = mid + 1

        return res