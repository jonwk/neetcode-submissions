class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]

        for i in range (n+1):
            res.append(res[i//2] + i%2)
        
        return res