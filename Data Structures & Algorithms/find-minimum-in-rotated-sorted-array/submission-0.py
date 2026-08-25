class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l, r = 0, len(nums)-1

        while l<r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r-1)//2
            res = min(nums[m], res)

            if res < nums[m]:
                l+=1
            else:
                r-=1

        
        return res
        