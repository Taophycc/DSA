from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        sorted_s1 = sorted(s1)

        for i in range(n - k+1):
            current_window = sorted(s2[i:i+k])

            if current_window == sorted_s1:
                return True
    
        return False