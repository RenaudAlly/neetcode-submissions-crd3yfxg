class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Goal: Identify cell that is able to reach (top or left edge) and (bottom or right) edge
        # Approach: Try a recursive aproach to identify neighbors that can reach both oceans
        #
        # Pseudocode
        # For the pacific ocean, do a dfs search start from the top left node (m + n)
        # Every node that is greater than or equal to the curret node can have water flow into it, add it to the list of pacific
            
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def dfs(r, c, visit, prevHeight):
            # Checking if we should call dfs or not
            if (
                (r not in range(rows)) or
                (c not in range(cols)) or
                ((r, c) in visit) or
                (heights[r][c] < prevHeight)
            ):
                return
            
            visit.add((r, c))

            # Calling dfs function on all the neighbors
            directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # Set of all nodes that are connected to pacific and atlantic
        both = pacific.intersection(atlantic)

        return [[i , j] for i, j in both]