class Solution:
    def findMin(self, nums: List[int]) -> int:     
        n = len(nums)
        l, r = 0, n - 1

        # Algorithm
        while l < r:
            m = l + (r - l) // 2 # finding midpoint

            if nums[m] > nums[r]: # look right if mid is greater than right (minimum must lie there)
                l = m + 1
            else: # when mid is smaller than right
                r = m

        return nums[l]
