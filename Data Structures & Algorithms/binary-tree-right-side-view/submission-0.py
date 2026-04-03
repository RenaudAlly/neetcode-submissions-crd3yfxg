# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Approach
        # We do a BFS traversal, at the end of adding each neighbor, 
        # we take a peek and add it to res

        # Edge case
        if not root:
            return []

        res = [root.val] # first node is guaranteed to be right visible

        q = deque()
        q.append(root)

        def bfs():
            while q: # while q is not empty
                # We only want to add at the end of a graph level
                # Key insight: 
                for _ in range(len(q)):
                    v = q.popleft()

                    # adding each neighbor to the q
                    if v.left:
                        q.append(v.left)
                    if v.right:
                        q.append(v.right)

                # taking peek at q tail after adding all the nodes in the level
                if q:
                    res.append(q[-1].val)

        bfs()
        return res