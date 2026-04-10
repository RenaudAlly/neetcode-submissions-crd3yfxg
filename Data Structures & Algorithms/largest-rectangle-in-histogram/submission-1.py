class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i # start of the bar we are considering

            while stack and stack[-1][1] > h: # height is greater than top of stack 
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) # get area of rectangle we just popped
                start = index
            
            stack.append((start, h))

        n = len(heights)
        for index, height in stack:
            maxArea = max(maxArea, height * (n - index))
        
        return maxArea