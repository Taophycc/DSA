class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #s>ABCABC - t>ABC
        # t/s ABC/ABCABC ABCABC = ABC
        # a, b = b, a%b
        # str2 is a gcd if it can divide str1 n times
        # ABCABC/ABC = ABC ABC can divide ABCABC 2 times FINAL DIVISOR ABC
        # ABABAB/ ABAB = AB - ABAB cannot divide ABABAB,  AB/ ABAB, FINAL DIVISOR IS AB
        # LEET/CODE = ""
        # AAAAAB/AAA = AAA can't divide AAAAAB, AAB/AAA CANT DIVIDE ANY FURHTER
        n, m = len(str1), len(str2)

        if str1 + str2 != str2 + str1:
            return ""
            
        def gcd(a, b):
            while b:
                a, b = b , a % b
            return a
        x = gcd(n, m)
        
        return str1[0:x]