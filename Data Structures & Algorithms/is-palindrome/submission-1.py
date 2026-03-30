class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i points at the start of the string
        # j points to end of the string

        # Making the string case-insensitve and remove non-alphanumerical chars
        s = s.lower()
        sanitized_s = ""
        for char in s:
            if char.isalnum():
                sanitized_s += char
        
        print(sanitized_s)
        i = 0
        j = len(sanitized_s) - 1

        while i < j:
            if sanitized_s[i] != sanitized_s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True