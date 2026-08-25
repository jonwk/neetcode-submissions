class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ptr1, ptr2 = 0, 1

        if len(s) <= 1:
            return len(s)
        
        chars = s[ptr1]
        maxLen = 1
        while ptr1 < ptr2 < len(s):
            maxLen = max(maxLen, len(chars))
            
            if s[ptr1] != s[ptr2] and s[ptr2] not in chars:
                chars += s[ptr2]
                ptr2 += 1
            else:
                ptr1 = ptr2
                chars = s[ptr1]
                ptr2 += 1
        
        return maxLen

        