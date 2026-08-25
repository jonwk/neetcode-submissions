class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)

        freq = [[]for i in range(len(nums)+1)]

        for n, c in count.items():
            freq[c].append(n)


        res = []
        index = len(freq) - 1
        target = 0
        for n in freq[index]:
            res.append(n)
            if len(res)==k:
                return res
            index -= 1