class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        sum = 0
        div = 2
        binArr = [0]

        for i in range(n+1):
            if i>0 and i % div == 0:
                div = i
                sum = i//div 
                print('if', i, div, sum)
            else:
                sum += ((i % div)-(i//div))
                print('else',i, div, sum)
            res.append(sum)

        return res