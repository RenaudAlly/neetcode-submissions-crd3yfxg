"""
00 01 02 03
10 11 12 13
20 21 22 23

l + (r - l) // 2

Pseudocode: 

- Identify which row it might belong to (iterate through 0th index in each list)
    - Binary search on the rows
- Search through the array we have narrowed down 
    - Binary search

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix) -1, len(matrix[0]) - 1

        # Searching through the rows
        row = -1
        t, b = 0, rows

        while t <= b:
            m = (t + b) // 2 # functions as row index

            if matrix[m][0] <= target <= matrix[m][cols]:
                row = m
                break
            elif target < matrix[m][0]:
                b = m - 1
            else:
                t = m + 1
        
        # Guard clause to check if we found a row
        if row == -1:
            return False
        
        cols = len(matrix[0]) - 1
        l, r = 0, cols

        while l <= r:
            m = (l + r) // 2 # functions as col index

            if target == matrix[row][m]:
                return True
            elif target < matrix[row][m]:
                r = m - 1
            else:
                l = m + 1
        
        return False