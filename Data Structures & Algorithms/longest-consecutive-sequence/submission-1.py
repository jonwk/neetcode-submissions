class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = []
        for i in nums:
            if i not in unique:
                unique.append(i)
        
        unique.sort()

        maxLength = 0

        if len(unique) <= 1:
            return len(unique)
        l, r = 0, 1
        
        curr = 0
        while r<len(unique):
            if unique[r]-unique[l] == 1:
                curr+=1
            else:
                maxLength = max(maxLength, curr)
                curr = 0
            l+=1
            r+=1

        return maxLength
            


        