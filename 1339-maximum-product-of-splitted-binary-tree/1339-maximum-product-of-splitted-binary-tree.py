# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum product of two subtrees formed by splitting the binary tree.
        
        Strategy:
        1.  **Postorder DFS:** Visit every node to calculate the sum of the subtree rooted at that node.
        2.  **Collection:** Store the sum of EVERY subtree in a list (`all_sum`). 
            These values represent the sum of the subtree we are "cutting off."
        3.  **Total Sum:** The DFS returns the sum of the entire tree.
        4.  **Math Optimization:** For each subtree sum 's':
                Remaining Tree Sum = Total Sum - s
                Product = s * Remaining Tree Sum
            
        Complexity:
            Time: O(N) - We visit every node once.
            Space: O(N) - To store the recursion stack and the list of sums.
        """
        all_sum = []
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            current_sum = node.val + left + right
            all_sum.append(current_sum)

            return current_sum

        total_sum = dfs(root)
        max_product = 0

        for s in all_sum:
            curr_product = s * (total_sum - s)
            max_product = max(curr_product, max_product)
        return max_product % (10**9 + 7)