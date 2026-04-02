# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        def dfs(root):
            if not root:
                return 0
            
            leftPath = dfs(root.left)
            rightPath = dfs(root.right)

            if leftPath == -1 or rightPath == -1 or abs(leftPath - rightPath) > 1:
                return -1
            
            return 1 + max(leftPath, rightPath)

        return dfs(root) != -1