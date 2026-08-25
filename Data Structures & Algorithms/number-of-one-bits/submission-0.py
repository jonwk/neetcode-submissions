class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for _ in range(32):
            bit = n >> 1
            print(bit)
            n>>=1
        return res
        