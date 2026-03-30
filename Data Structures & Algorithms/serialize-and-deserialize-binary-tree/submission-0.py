# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes = []

        # Edge case
        if not root:
            return ""
        
        q = deque()
        q.append(root)

        def bfs(node):
            while q:
                node = q.popleft()

                if node:
                    # Adding value
                    nodes.append(str(node.val))
                    # Adding children (even if they are none)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    nodes.append("N")
                
        bfs(0)
        res = ','.join(nodes)
        return res
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Edge case
        if data == "":
            return None
        
        # Creating root node
        data = data.split(",")
        root = TreeNode(data[0], None, None)

        # Starting BFS creation
        i = 1
        q = deque([root])

        while q:
            node = q.popleft()

            if i < len(data) and data[i] != 'N':
                leftChild = TreeNode(data[i], None, None)
                q.append(leftChild) # adding nodes with unassigned children
                node.left = leftChild # assigning node
            if (i + 1) < len(data) and data[i + 1] != 'N':
                rightChild = TreeNode(data[i + 1], None, None)
                q.append(rightChild)
                node.right = rightChild

            i += 2
        
        return root