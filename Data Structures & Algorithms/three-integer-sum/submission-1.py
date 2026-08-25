class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = nums.sorted()
        minNum = nums[0]
        for index, num in enumerate(nums):
            left, right = index+1, len(nums)-1
            sum = minNum + nums[left] + nums[right]
            if sum == 0:
                res.append([minNum, nums[left], nums[right]])
                minNum = nums[left]
            elif sum > 0:
                right -= 1
            else:
                left += 1
        return res