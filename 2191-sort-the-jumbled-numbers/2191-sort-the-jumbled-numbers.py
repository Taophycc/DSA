class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
            def translate(num):
                res = []
                s = str(num)

                for char in s:
                    original_digit = int(char)
                    mapped_digit = mapping[original_digit]
                    res.append(str(mapped_digit))
                return int("".join(res))
            nums.sort(key = translate)
            return nums