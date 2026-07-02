class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        merged = []

        l,r = 0, 0

        while l < n and r < m:
            merged += word1[l] + word2[r]
            l += 1
            r += 1

        merged.append(word1[l:])
        merged.append(word2[r:])

        return "".join(merged)