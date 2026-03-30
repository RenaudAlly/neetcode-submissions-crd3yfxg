class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary for mapping character count tuple to words
        anagram_groups = defaultdict(list)

        for word in strs:
            
            # Using array as key for dict 
            count = [0] * 26
            # Counting frequency
            for char in word:
                count[ord(char) - ord('a')] += 1

            # Mapping count to word 
            anagram_groups[tuple(count)].append(word)
        
        return list(anagram_groups.values())
        