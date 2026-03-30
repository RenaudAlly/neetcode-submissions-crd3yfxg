class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case for empty string
        if t == "":
            return ""

        countT, window = defaultdict(int), defaultdict(int)

        # T is unchanging and we need it for checking our conditions
        for c in t:
            countT[c] += 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('infinity')

        # Executing core algorithm
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # updating the result
                window_size = r - l + 1
                if window_size < resLen:
                    res = [l, r]
                    resLen = window_size
                # popping from left to make the window as small as possible
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                # since we are popping we upate the left pointer
                l += 1

        # Returning result as per format
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""