class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Pseudocode
        # Iterating through the array backwards 
        #   If curr temperature is greater than top of stack (assuming stack is non-empty), keep popping until top is greater or empty
        #   If curr temperature is lesser than top of stack, record value, push onto the stack

        n = len(temperatures)
        results = [0] * n

        stack = []

        for i in range(n - 1, -1, -1):
            if not stack or temperatures[i] < stack[-1][1]:
                if not stack:
                    results[i] = 0
                else:
                    results[i] = stack[-1][0] - i
                    
                stack.append((i, temperatures[i]))
            else:
                while stack and (stack[-1][1] <= temperatures[i]):
                    stack.pop()
                
                if not stack:
                    results[i] = 0
                else:
                    results[i] = stack[-1][0] - i

                stack.append((i, temperatures[i]))
        
        return results