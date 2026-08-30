class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i, j = 0, 1
        n = len(arr)
        while j < n:
            arr[i] = max(arr[j:])
            i = j
            j += 1
        
        arr[j-1] = -1
        return arr