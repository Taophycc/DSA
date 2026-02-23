class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        len_s = len(s)
        for i in range(len_s - k+1):
            if len(seen) == 2**k:
                break

            temp = int(s[i:i+k], 2)
            if temp not in seen:
                seen.add(temp)

        for j in range(2**k):
            if j not in seen:
                return False
        
        return True