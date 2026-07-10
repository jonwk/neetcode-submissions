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
        
        print(unique)
        curr = 1
        while r<len(unique):
            if unique[r]-unique[l] == 1:
                print(unique[l], curr)
                curr+=1
            else:
                curr = 1
            maxLength = max(maxLength, curr)
            l+=1
            r+=1

        return maxLength
            


        