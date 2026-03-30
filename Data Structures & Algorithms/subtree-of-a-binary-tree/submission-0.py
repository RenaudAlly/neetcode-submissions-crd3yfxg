# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper method: Checking if the two trees are the same
        def isIdentical(root, subRoot):
            # base case
            if not root and not subRoot:
                return True

            if not root or not subRoot or root.val != subRoot.val:
                return False
            
            # recursive case
            return root.val == subRoot.val and isIdentical(root.left, subRoot.left) and isIdentical(root.right, subRoot.right)

        # base case 
        if not root:
            return False
        
        # checking for the top node
        if isIdentical(root, subRoot):
            return True
        
        # Checking children subtrees
        left_branch = self.isSubtree(root.left, subRoot)
        right_branch = self.isSubtree(root.right, subRoot)
        
        return left_branch or right_branch