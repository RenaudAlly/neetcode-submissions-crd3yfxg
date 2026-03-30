class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # 1. Create indexable arrays filled with 1s
        prefix = [1] * n
        postfix = [1] * n
        result = [1] * n

        # 2. Build prefix array (left to right)
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]

        # 3. Build postfix array (right to left)
        postfix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        # 4. Calculate the result
        for i in range(n):
            # If at the beginning, there is no left prefix, default to 1
            left_product = prefix[i - 1] if i > 0 else 1
            
            # If at the end, there is no right postfix, default to 1
            right_product = postfix[i + 1] if i < n - 1 else 1
            
            result[i] = left_product * right_product

        return result