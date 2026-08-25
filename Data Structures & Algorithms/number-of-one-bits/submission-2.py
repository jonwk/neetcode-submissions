class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n >> i & 1
            print(bit)
            n>>=1
        return res
        