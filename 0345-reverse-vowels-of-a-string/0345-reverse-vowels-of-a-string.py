class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        chars = list(s)

        l, r = 0, len(chars) - 1

        while l < r:
            while l < r and chars[l] not in vowel_set:
                l += 1
            while l < r and chars[r] not in vowel_set:
                r -= 1

            if l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l+=1
                r-=1

        return "".join(chars)