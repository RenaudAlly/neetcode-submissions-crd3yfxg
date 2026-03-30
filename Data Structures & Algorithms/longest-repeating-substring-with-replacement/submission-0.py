# XYX, k = 0
# output: 1

# XYZZ , k = 1
# output = 3 

# XYYX, k = 1
# output = 3

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       # Approach: Using a sliding window to keep track of the valid string

       # Pseudocode
       # Keeping track of the chars in the current window
       # Initialize window with i and j
       # increment j pointer until we exhaust k (k should be less than window size - count of most common char)
       # To replenish k, we increment the i pointer 
       # Continue until j reaches the end of the string

       # Count: X = 1, Y = 1

        i, j = 0, 0
        max_length = 1 # list will be atleast 1 in size
        counter = defaultdict(int)

        for j in range(len(s)):
            # increment char count
            counter[s[j]] += 1
            char_count = max(counter.values()) # getting occurence of most common char

            # incrementing j while valid
            window_size = j - i + 1
            if k >= (window_size - char_count):
                max_length = max(max_length, window_size)
            else: # k has been exhausted, need to shrink window (from the left)
                counter[s[i]] -= 1
                i += 1
        
        return max_length