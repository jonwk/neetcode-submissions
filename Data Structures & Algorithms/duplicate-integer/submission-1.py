class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for n in nums:
            if n in vals:
                return True
            else:
                vals[n] = 1
        return False