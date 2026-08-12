# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(node):
            if not node:
                return None
            
            if node.left:
                inorder(node.left)
            
            if node:
                res.append(node.val)
            
            if node.right:
                inorder(node.right)
        inorder(root)
        return res

            

        