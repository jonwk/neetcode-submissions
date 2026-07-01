class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            req = target - nums[i]
            if req in seen:
                return [seen[req],i]
            else:
                seen[val] = i