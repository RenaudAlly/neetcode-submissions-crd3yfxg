"""
We want to find out the minimum bananas monkey can eat at once

[1, 4, 3, 2]

Koko has 9 hours. Max he can eat at once is. Least he can eat is 1

ceil(x / k) is the time it will take to finish. 

Highest value for k can be max(piles) which is m

[25, 10, 23, 4]

The most koko can eat at once is the max height of the pile. 
Brute force solution would be to check all the piles from 1 to said m 

Instead of seeing if koko can eat the bananas all the way from 1 to m,
we check if koko can eat mid way, if she can, look at left half else second half

How do we check if Koko can finish the bananas?

canFinishBananas(k) -> bool
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Function checking if all the bananas can be eaten
        def canFinishBananas(k):
            total_time = 0

            for pile in piles:
                finish_time = math.ceil(pile / k)
                total_time += finish_time
            
            return True if total_time <= h else False
        
        # Finding minimum eating rate
        m = max(piles) # highest value of k

        l = 1
        r = m

        while l <= r:
            mid = (l + r) // 2

            if canFinishBananas(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l