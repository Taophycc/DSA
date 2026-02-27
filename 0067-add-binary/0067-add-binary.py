class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i>=0 else 0
            bit_b = int(b[j]) if j>=0 else 0

            total = bit_a + bit_b + carry
            res.append(str(total & 1))
            carry = total >> 1
            i -= 1
            j -= 1
            
        return "".join(res[::-1])