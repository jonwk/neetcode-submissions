class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        unique = set(nums)
        print(unique)
        return unique[:k]


