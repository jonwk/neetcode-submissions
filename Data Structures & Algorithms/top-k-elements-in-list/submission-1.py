class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        set = OrderedDict.fromkeys(nums)
        
        return set[:-k]


