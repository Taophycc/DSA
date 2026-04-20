class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0
        for i in range(n):
            for j in range(1, n):
                if colors[i] == colors[j]:
                    continue
                res = max(res, abs(i-j))
        return res
