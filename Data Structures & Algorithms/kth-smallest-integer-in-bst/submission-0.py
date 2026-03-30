# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We know that it's a valid subtree

        def inOrder(node, traversal):
            if not node:
                return

            inOrder(node.left, traversal)
            traversal.append(node.val)
            inOrder(node.right, traversal)

            return traversal
        
        res = inOrder(root, traversal = [])

        # getting index of the kth-smallest value
        i = k - 1
        return res[i]