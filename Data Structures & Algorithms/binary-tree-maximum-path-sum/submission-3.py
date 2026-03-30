# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            # Getting nodes values
            leftNode = dfs(root.left)
            rightNode = dfs(root.right)
            rootNode = root.val

            # Paths
            path1 = leftNode + rootNode
            path2 = rightNode + rootNode
            paths = max(path1, path2, rootNode)

            # Checking for fork
            fork = leftNode + rootNode + rightNode

            # Recording max value so far but only returning non-fork values (so we can maintain a straight line)
            res = max(res, paths, fork)
            return paths
        
        dfs(root)

        return res