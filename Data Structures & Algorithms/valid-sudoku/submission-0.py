from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 1. Check for duplicates in every row
        for i in range(9):
            # board[i] grabs the entire row automatically
            if self.check_dups(board[i]):
                return False

        # 2. Check for duplicates in every column
        for i in range(9):
            # List comprehension: grab the i-th element from every row 'r'
            column = [board[r][i] for r in range(9)]
            if self.check_dups(column):
                return False

        # 3. Check for duplicates in every 3x3 sub-box
        # Step by 3 to hit the top-left corner of each box (0, 3, 6)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # Safely extract all 9 values with proper [row][col] formatting
                values = [
                    board[i][j],     board[i][j + 1],     board[i][j + 2],
                    board[i + 1][j], board[i + 1][j + 1], board[i + 1][j + 2],
                    board[i + 2][j], board[i + 2][j + 1], board[i + 2][j + 2]
                ]
                
                if self.check_dups(values):
                    return False
        
        return True

    def check_dups(self, values: List[str]) -> bool:
        # A set is slightly more efficient here since we just need to check for existence
        seen = set()
        for value in values:
            if value != '.':
                if value in seen:
                    return True
                seen.add(value)
        return False