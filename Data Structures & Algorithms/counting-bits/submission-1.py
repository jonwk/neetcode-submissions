class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            binary = format(i, 'b')
            sum = sum(binary.split(''))
            print(binary)