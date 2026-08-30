class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutive = 0

        if len(nums) == 1:
            return 1 if nums[0] == 1 else 0
        
        curr = 0

        for i in nums:
            if i == 1:
                curr+=1
                print(i, curr)
            
            else:
                curr = 0

            maxConsecutive = max(curr, maxConsecutive)

        return maxConsecutive


        

        