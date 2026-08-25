class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, 1
        nums.sort()
        while r < len(nums):
            diff = nums[r] - nums[l]
            if diff != 1:
                return nums[l] + diff
            l = r
            r += 1
        return 0
        