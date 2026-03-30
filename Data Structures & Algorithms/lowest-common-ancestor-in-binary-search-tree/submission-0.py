# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Important assumptions: 
        # 1. No duplicates
        # 2. Unique value
        # 3. p != q
        pval, qval = p.val, q.val


        if pval <= root.val <= qval or qval <= root.val <= pval:
            return root
        elif pval < root.val and qval < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif pval > root.val and qval > root.val:
            return self.lowestCommonAncestor(root.right, p, q)