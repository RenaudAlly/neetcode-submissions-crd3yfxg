class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Converting array to a hash map
        hmap = {}
        for num in nums:
            hmap[num] = True

        # Getting start of sequence
        longestSequence = 0
        for num in nums:
            if num - 1 not in hmap:
                # Counting sequence length 
                currentSequence = 0
                check = num
                while True:
                    if check in hmap:
                        currentSequence += 1
                        check += 1
                    else:
                        break

                longestSequence = max(currentSequence, longestSequence)
        
        return longestSequence