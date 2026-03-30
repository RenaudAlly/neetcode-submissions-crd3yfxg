class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # If midpoint is not the target value, continue search: 

        # Which section of the array (sorted section, unsorted) is the target going to be in:
        n = len(nums)
        l, r = 0, n - 1

        res = -1

        while l <= r:
            m = l + (r - l) // 2

            # Checking if target found (early exit)
            if nums[m] == target:
                res = m
                break
            elif (nums[m] > nums[r] and not nums[l] <= target < nums[m]) or \
            (nums[m] < nums[r] and nums[m] < target <= nums[r]):
                l = m + 1
            else:
                r = m - 1
            
        return res