class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Algorithm 
        # If char in set, shrink the window until the OG copy is gone

        seen_chars = set()
        longest_seq = 0

        l = 0
        for r in range(len(s)):
            # Handling duplicates
            while s[r] in seen_chars:
                seen_chars.remove(s[l])
                l += 1
            
            seen_chars.add(s[r])

            longest_seq = max(longest_seq, r - l + 1)
        
        return longest_seq