class Solution:
    def validPalindrome(self, s: str) -> bool:
        # pal check, if char are same move pointers, else delete right or left by moving pointer forward and checking if they are pal again
        n = len(s)
        l, r = 0 , n - 1

        # inner palindrome check
        def is_pal (s, l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        # outer palindrome check
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                left = is_pal(s, l+1, r)
                right = is_pal(s, l, r-1)
                return left or right
        
        return True
        

