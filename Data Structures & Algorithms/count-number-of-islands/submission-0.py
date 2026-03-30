class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Algorithm
        # Using BFS to visit neighboars only if it's an island, and keep visiting

        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q: # while queue is not empty
                r, c = q.popleft()
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    if ((r + dr) in range(rows) and
                        (c + dc) in range(cols) and
                        grid[r + dr][c + dc] == "1" and
                        (r + dr, c + dc) not in visited
                    ):
                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))


        for r in range(rows):
            for c in range(cols):
                # checking if island 
                    if grid[r][c] == "1" and (r, c) not in visited:
                        bfs(r, c)
                        islands += 1
        
        return islands