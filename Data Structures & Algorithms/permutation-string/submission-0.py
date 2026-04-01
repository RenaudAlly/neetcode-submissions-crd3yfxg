# Gemini solution: Spent too long on this so I'm moving on

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: s1 cannot be longer than s2
        if len(s1) > len(s2):
            return False
            
        # Create a frequency map for s1
        s1_count = Counter(s1)
        
        # Create an initial window of the same size for s2
        window_size = len(s1)
        window_count = Counter(s2[:window_size])
        
        # Check the very first window
        if s1_count == window_count:
            return True
            
        # Slide the fixed window exactly one character at a time
        for i in range(window_size, len(s2)):
            # 1. Add the new character on the right
            new_char = s2[i]
            window_count[new_char] += 1
            
            # 2. Remove the old character that fell off the left
            old_char = s2[i - window_size]
            window_count[old_char] -= 1
            
            # 3. Clean up 0-counts so dictionary equality works perfectly
            if window_count[old_char] == 0:
                del window_count[old_char]
                
            # 4. Check if we found a match
            if s1_count == window_count:
                return True
                
        return False