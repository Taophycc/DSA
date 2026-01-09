# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return node, 0

            left_subtree, left_depth = dfs(node.left)
            right_subtree, right_depth = dfs(node.right)
            

            if left_depth > right_depth:
                return left_subtree, left_depth +1 
            elif right_depth > left_depth:
                return right_subtree, right_depth +1 
            else:
                return node, left_depth + 1
        final_node, final_depth = dfs(root)

        return final_node