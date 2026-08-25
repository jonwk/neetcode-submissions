class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        allNums = range(min(nums), max(nums)+1)
        return sum(allNums) - sum(nums)
        