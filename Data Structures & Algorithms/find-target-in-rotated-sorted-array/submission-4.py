class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0

        l, r = 0, len(nums)-1

        while l<=r:
            if nums[l] < nums[r]:
                res+=1
                break
            
            m = (l+r)//2
            res+=1
            if nums[m] >= nums[l]:
                res+=1
                l = m+1
            else:
                res+=1
                r = m-1

        
        return res