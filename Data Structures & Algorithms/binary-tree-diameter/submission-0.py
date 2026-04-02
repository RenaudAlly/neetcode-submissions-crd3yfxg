# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0

        def dfs(root):
            nonlocal d

            if not root:
                return 0

            leftPath = 1 + dfs(root.left) if root.left else 0
            rightPath = 1 + dfs(root.right) if root.right else 0

            midPath = leftPath + rightPath

            if midPath > d:
                d = midPath

            return max(leftPath, rightPath)

        return max(dfs(root), d)