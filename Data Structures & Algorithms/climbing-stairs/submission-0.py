class Solution:
    def climbStairs(self, n: int) -> int:
        penultimate, last = 1, 1
        for i in range(n-1):
            temp = penultimate
            penultimate = last + penultimate
            last = temp

        return penultimate
        