# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0,0]
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            steal = node.val + leftSum[1] + rightSum[1]
            not_steal = max(leftSum) + max(rightSum)

            return [steal, not_steal]
        
        return max(dfs(root))
        