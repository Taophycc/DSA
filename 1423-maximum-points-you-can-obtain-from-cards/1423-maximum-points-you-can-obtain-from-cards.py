class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        max_sum, forward_sum, backward_sum = 0, 0, 0

        for i in range(k):
            forward_sum += cardPoints[i]
        max_sum = forward_sum
        
        right_index = n - 1
        for i in range(k - 1, -1, -1):
            forward_sum -= cardPoints[i]
            backward_sum += cardPoints[right_index]
            right_index -= 1
            max_sum = max(max_sum, forward_sum + backward_sum)

        return max_sum