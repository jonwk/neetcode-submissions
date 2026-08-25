class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, 1
        nums.sort()
        while r < len(nums):
            diff = nums[r] - nums[l]
            if diff == 1:
                l = r
                r += 1
            else:
                return nums[l]+diff
        return 0
        