from collections import Counter
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:

        count_even_s1 = Counter(s1[0::2])
        count_even_s2 = Counter(s2[0::2])

        count_odd_s1 = Counter(s1[1::2])
        count_odd_s2 = Counter(s2[1::2])

        if count_even_s1 == count_even_s2 and count_odd_s1 == count_odd_s2:
            return True
            
        return False