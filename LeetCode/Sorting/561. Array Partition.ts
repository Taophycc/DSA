// Difficulty - EASY
/*
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        def quickSort(arr, low, high):
            if (low >= high):
                 return arr

            l = low
            h = high
            mid = l+ (h-l)//2
            pivot = arr[mid]

            while(l<= h):
                while(arr[l] < pivot):
                    l+=1
                while(arr[h] > pivot):
                    h-=1

                if(l<=h):
                    temp = arr[l]
                    arr[l] = arr[h]
                    arr[h] = temp
                    l+=1
                    h-=1
            quickSort(arr, low, h)
            quickSort(arr, l, high)

        quickSort(nums, 0, len(nums) - 1)
        return sum(nums[i] for i in range(0, len(nums), 2))
*/
/*
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))
*/
