# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        queue.append(root)

        curr_level = 1
        final_level = 0
        max_sum = float('-inf')

        while queue:
            curr_sum = 0
            level_size = len(queue)

            for _ in range(len(queue)):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if curr_sum > max_sum:
                max_sum = curr_sum
                final_level = curr_level
            curr_level += 1

        return final_level