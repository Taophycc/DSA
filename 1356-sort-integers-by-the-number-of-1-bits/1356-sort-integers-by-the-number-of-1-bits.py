class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def get_bit_cnt(num):
            count = 0
            while num > 0:
                if num & 1:
                    count += 1
                num >>=1
            return count

        arr.sort(key = lambda x : (get_bit_cnt(x), x))
        return arr
        # TC - O(N.log(N)) Python's Tim Sort
        # SC - O(N) lambda function in sort creates extra tuples of size N