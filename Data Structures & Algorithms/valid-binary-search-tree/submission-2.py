# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversal = []

        def inOrder(node, traversal):
            if not node:
                return

            inOrder(node.left, traversal) # adds vals in left subtree
            traversal.append(node.val) # adding current node
            inOrder(node.right, traversal)

            return traversal

        # In-order traversal of BST
        inOrder(root.left, traversal)
        traversal.append(root.val)
        inOrder(root.right, traversal)

        # Checking if increasing order
        for i in range(len(traversal) - 1):
            if traversal[i + 1] <= traversal[i]:
                return False
        
        return True