class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        if not nums:
            return []
        for index, num in enumerate(nums):
            left, right = index+1, len(nums)-1
            if index<0 and num != nums[left]:
                while left < right:
                    sum = num + nums[left] + nums[right]
                    if sum == 0:
                        res.append([num, nums[left], nums[right]])
                    elif sum > 0:
                        right -= 1
                    else:
                        left += 1
        return res