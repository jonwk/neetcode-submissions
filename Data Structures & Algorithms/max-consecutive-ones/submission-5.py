class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutive = 0
        curr = 0

        for i in nums:
            if i == 1:
                curr+=1
            
            else:
                curr = 0

            maxConsecutive = max(curr, maxConsecutive)

        return maxConsecutive


        

        