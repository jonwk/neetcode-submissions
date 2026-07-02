class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        for char in s:
            if char in s_set:
                s_set[char]+=1
            else:
                s_set[char]=1
        
        for char in t:
            if char not in s_set:
                return False
            else:
                s_set[char] -= 1
        
        for i in s_set.values():
            if i!=0:
                return False
        
        return True