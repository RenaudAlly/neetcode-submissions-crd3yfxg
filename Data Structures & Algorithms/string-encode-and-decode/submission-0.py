class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_strings = ""

        for word in strs:
            encoded_string = str(len(word)) + '#' + word
            encoded_strings += encoded_string
        
        return encoded_strings

    def decode(self, s: str) -> List[str]:
        # Algorithm
        # 1. Getting length of word
        # 2. Reading the entire word
        decoded_strings = []

        # Finding the indices 
        i = 0
        while i < len(s):
            j = i
            # 1. getting decoded string length
            while s[j] != "#":
                j += 1
        
            decoded_string_length = int(s[i:j])
            
            # 2. getting decoded string
            decoded_string = s[j+1:j+1+decoded_string_length]

            # 3. adding decoded string
            decoded_strings.append(decoded_string)

            # Updating pointer position
            i = j + decoded_string_length + 1

        return decoded_strings

