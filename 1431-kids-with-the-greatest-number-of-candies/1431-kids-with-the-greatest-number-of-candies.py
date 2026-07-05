class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # [2,3,5,1,3]
        n = len(candies)
        gr = max(candies)
        res = [False] * n

        for i in range(n):
            if candies[i] + extraCandies >= gr:
                res[i] = True
        print(res)
        return res