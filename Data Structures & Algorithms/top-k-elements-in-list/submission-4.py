class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        unique = OrderedDict.fromkeys(nums)
        print(unique)
        return unique[:k]


