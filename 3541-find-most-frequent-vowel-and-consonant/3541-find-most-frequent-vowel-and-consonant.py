from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)
        max_vowel_cnt = 0
        max_consonant_cnt = 0

        for char, freq in count.items():
            if char in 'aeiou':
                max_vowel_cnt = max(max_vowel_cnt, freq)
            else:
                max_consonant_cnt = max(max_consonant_cnt, freq)

        return max_vowel_cnt + max_consonant_cnt

