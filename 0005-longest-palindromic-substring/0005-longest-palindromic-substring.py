class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                nonlocal start, end
                if (r-l) > (end - start):
                    start = l
                    end = r
                l -= 1
                r += 1
        
        for i in range(n):
            # odd len palindromes
            expand(i, i)
            # even len palindromes
            expand(i, i+1)
            
        return s[start:end + 1]