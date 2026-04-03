class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(val, choose):
            # breaking condition
            if len(val) == n:
                res.append(val.copy())
                return
            
            # picking the values that haven't been chosen
            for i in range(n):
                if not choose[i]: # when it is false
                    # we need 
                    choose[i] = True
                    val.append(nums[i])

                    dfs(val, choose)

                    choose[i] = False
                    val.pop()

        choose = [False] * n
        dfs([], choose) # initial dfs call
        return res