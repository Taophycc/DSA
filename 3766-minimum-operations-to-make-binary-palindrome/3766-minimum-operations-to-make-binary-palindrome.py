class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        def is_binary_palindrome(n):
            s = bin(n)[2:]
            return s == s[::-1]

        res = []

        for num in nums:
            # case 1: num is a palindrome, no of operations is 0
            if is_binary_palindrome(num):
                res.append(0)
                continue

            diff = 1
            
            while True:
            # case 2:
                # edgecase - we cant find the binary of negatives
                # searching downwards
                if (num - diff) >= 0 and is_binary_palindrome(num - diff):
                    res.append(diff)
                    break
                # searching upwards
                if is_binary_palindrome(num + diff):
                    res.append(diff)
                    break
                diff += 1

        return res