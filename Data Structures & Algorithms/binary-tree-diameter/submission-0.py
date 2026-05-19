# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
          self.diameter = 0

          def depthFirstSearch(node):
                if not node:
                     return 0
                
                while node:
                     left_depth = depthFirstSearch(node.left)
                     right_depth = depthFirstSearch(node.right)

                     self.diameter = max(self.diameter, left_depth + right_depth)

                     return max(left_depth, right_depth) + 1
                
          depthFirstSearch(root)
          return self.diameter
                

      