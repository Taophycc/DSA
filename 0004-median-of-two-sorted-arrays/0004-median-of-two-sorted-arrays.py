class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        l, r = 0, n1
        while l <= r:
            cut1 = (l + r) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1

            left1 = nums1[cut1 - 1] if cut1 != 0 else float('-inf')
            left2 = nums2[cut2 - 1] if cut2 != 0 else float('-inf')

            right1 = nums1[cut1] if cut1 != n1 else float('inf')
            right2 = nums2[cut2] if cut2 != n2 else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (n1 + n2) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                r = cut1 - 1
            else:
                l = cut1 + 1
        return 0