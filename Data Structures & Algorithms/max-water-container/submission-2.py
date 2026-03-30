class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Algorithm
        # Start from the edges (left and right pointer), calculate area
        n = len(heights)

        l = 0
        r = n - 1

        max_area = 0
        while l < r:
            # calculating current area
            height = min(heights[l], heights[r])
            width = r - l
            cur_area = height * width
            max_area = max(max_area, cur_area)

            # optimization step
            # we want to find the furthermost heights maximized
            # if l is lesser than right, then increment left 
            # elif l is greater than right, then we decrement right
            # else, just move any?

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_area