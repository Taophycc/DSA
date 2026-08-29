class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            c = s[r]
            if c in last_seen and last_seen[c] >= l:
                l = last_seen[c] + 1
            last_seen[c] = r
            max_len = max(max_len, r-l+1)
        return max_len