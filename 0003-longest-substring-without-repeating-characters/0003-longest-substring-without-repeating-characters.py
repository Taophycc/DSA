class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = defaultdict(int)
        max_len = float('-inf')
        left = 0

        for right in range(n):
            char = s[right]
            seen[char] += 1

            while left < right and seen[char] > 1:
                if seen[s[left]] > 0:
                    seen[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max(max_len, 0)

