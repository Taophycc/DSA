class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        cnt = 0

        for i in range(length):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                cnt += 1
        return cnt >= n