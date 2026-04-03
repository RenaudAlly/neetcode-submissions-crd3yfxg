class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, val): # i is the decision element, val is the state as of now (not the same)
            # breaking condition 
            if i == len(nums):
                res.append(val.copy())
                return

            dfs(i + 1, val)
            dfs(i + 1, val + [nums[i]])
        
        dfs(0, [])
        return res