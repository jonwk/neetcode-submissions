class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, 1
        while r < len(nums):
            if nums[l]-nums[r] != 1:
                return nums[l]-nums[r]+1
            l = r
            r += 1
        return 0
        