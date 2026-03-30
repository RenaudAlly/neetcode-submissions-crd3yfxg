# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # for base tree
        if not p and not q:
            return True
        
        # if one node is missing
        if not p or not q:
            return False
        
        # if they are just unequal
        if p.val != q.val:
            return False

        # check both sides
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right