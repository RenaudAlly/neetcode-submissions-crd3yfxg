class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)

        ones = 0
        for char in s:
            if char == '1':
                ones += 1

        return ones