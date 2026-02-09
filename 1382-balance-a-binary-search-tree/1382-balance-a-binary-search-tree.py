# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        def dfs(node):
            if not node:
                return []
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)

        def buildTree(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(res[mid])

            node.left = buildTree(left, mid-1)
            node.right = buildTree(mid+1, right)

            return node

        return buildTree(0, len(res) - 1)