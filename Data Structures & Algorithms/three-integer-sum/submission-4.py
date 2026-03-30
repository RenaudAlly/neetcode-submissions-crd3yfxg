class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting the list
        nums = sorted(nums)

        triplets = []

        i = 0
        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
               cur = nums[i] + nums[l] + nums[r]

               if cur < 0:
                  l += 1
               elif cur > 0:
                  r -= 1
               else: # matches target 
                  triplets.append([nums[i], nums[l], nums[r]])

                  l += 1
                  r -= 1

                  while l < r and nums[l - 1] == nums[l]:
                    l += 1

            i += 1

        return triplets