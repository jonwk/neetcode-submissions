class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, num in enumerate(numbers):
            req = target - num
            if req in hashmap:
                return [index, hashmap[req]]
            else:
                hashmap[num] = index

      
        