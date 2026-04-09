"""
We need to find the maximum number that we have seen so far.

Brute force tactic is O(k * (n - k)). Finding the max from k values at most n times

Ideal solution would require keeping track of the max value in the window. 

Idea:
- Initialize a window of size 1, heap
- Increment window until size k is reached, add to heap
- Get max from heap, and add to res
- Move window
- Add element to heap
- Before adding to res, check if index in window, pop until in window. Add to res
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] # results array 
        h = []

        l, r = 0, k - 1

        # Creating initial heap
        for i in range(k):
            heapq.heappush(h, (-nums[i], i))
        res.append(-h[0][0])
        
        # Moving window
        l += 1
        r += 1

        # General algorithm
        while r < len(nums):
            # Adding element to heap
            heapq.heappush(h, (-nums[r], r))

            # Removing elements
            while h[0][1] < l or h[0][1] > r: 
                heapq.heappop(h)
            
            res.append(-h[0][0])

            # Moving window
            l += 1
            r += 1

        return res