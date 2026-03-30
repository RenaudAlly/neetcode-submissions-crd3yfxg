class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        rows, cols = len(board), len(board[0])
        path = set()
        
        def dfs(i, j, c):
            # base success case
            if c == n:
                return True
            # base failure cases
            if i not in range(rows) or j not in range(cols):
                return False
            if (i, j) in path:
                return False
            if board[i][j] != word[c]:
                return False

            # recursive case (calling all the neighbors)
            # if we reach this point then current char matches expected char
            path.add((i, j)) # adding it as visited so it's not re-used during the exploration

            res = (
                dfs(i, j - 1, c + 1) or
                dfs(i, j + 1, c + 1) or
                dfs(i - 1, j, c + 1) or
                dfs(i + 1, j, c + 1)
            )

            # we free the cell
            path.remove((i, j))

            return res
        
        # making initial recursive call but we need to do it for every cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
                    
        return False