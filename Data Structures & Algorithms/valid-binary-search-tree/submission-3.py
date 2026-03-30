# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrder(node, traversal):
            if not node:
                return

            inOrder(node.left, traversal) # adds vals in left subtree
            traversal.append(node.val) # adding current node
            inOrder(node.right, traversal)

            return traversal

        # In-order traversal of BST
        res = inOrder(root, traversal = [])

        # Checking if increasing order
        for i in range(len(res) - 1):
            if res[i + 1] <= res[i]:
                return False
        
        return True