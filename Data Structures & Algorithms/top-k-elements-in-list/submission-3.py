class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        unique = OrderedDict.fromkeys(nums)
        
        return unique[:k]


