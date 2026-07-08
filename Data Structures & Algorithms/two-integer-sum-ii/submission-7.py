class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, num in enumerate(numbers):
            req = target - num
            if req in hashmap:

                return [1+index, 1+hashmap[req]] if index < hashmap[req] else [1+hashmap[req], 1+index]
            else:
                hashmap[num] = index

      
        