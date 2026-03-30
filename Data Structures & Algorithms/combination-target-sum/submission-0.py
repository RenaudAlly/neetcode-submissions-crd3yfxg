class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # This will contain our results
        res = []

        # Defining the traversal function
        # i - current index of char we are allowed to add
        # cur - current combination
        # total - the total we have in the tree so far
        def dfs(i, cur, total):
            # successful base case
            if target == total:
                res.append(cur.copy())
                return
            # pruning case
            if i >= len(nums) or total > target:
                return
            
            # recursive case (taking both decisions)
            # branch 1 (including the current candidate)
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            # branch 2 (not including the current candidate)
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res