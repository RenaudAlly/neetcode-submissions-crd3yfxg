class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0
        
        def dfs(r, c):
            nonlocal res

            # base condition
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c)) # marking as visited

            # calculating area
            neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0]] 

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        # calling dfs on all the nodes
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    island_area = dfs(i, j)
                    res = max(res, island_area)
        
        return res