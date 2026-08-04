class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {1:0}

        def get_power(num):
            curr = num
            steps = 0

            while curr not in cache:
                if curr % 2 == 0:
                    curr //= 2
                    steps += 1
                elif curr % 2 == 1:
                    curr = 3 * curr + 1
                    steps += 1

            cache[num] = steps + cache[curr]

            return cache[num]

        powers = [(get_power(i), i) for i in range(lo, hi + 1)]
        powers.sort()

        return powers[k-1][1]