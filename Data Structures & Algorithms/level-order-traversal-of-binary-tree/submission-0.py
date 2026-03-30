# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        # base case
        if not root:
            return []
        
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            tmp = []

            for i in range(size):
                node = q.popleft()
                tmp.append(node.val)
                # Adding children to queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(tmp)
        
        return res