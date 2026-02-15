class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            counts = {}
            max_freq = 0
            distinct_count = 0

            for j in range(i, n):
                char = s[j]

                if char not in counts:
                    counts[char] = 0
                    distinct_count += 1
                
                counts[char] += 1

                max_freq = max(max_freq, counts[char])

                curr_len = j - i + 1
                if max_freq * distinct_count == curr_len:
                    max_len = max(max_len, curr_len)

        return max_len