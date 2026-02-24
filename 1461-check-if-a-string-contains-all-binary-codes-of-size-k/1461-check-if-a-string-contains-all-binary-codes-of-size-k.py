class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        len_s = len(s)
        # 1 << k same as 2**k
        for i in range(len_s - k+1):
            seen.add(s[i:i+k])

            if len(seen) == 1 << k:
                return True

        return False