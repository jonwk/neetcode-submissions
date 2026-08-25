class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            binary = format(i, 'b')
            # ones = sum(binary.split(''))
            print(binary,binary.split(''))