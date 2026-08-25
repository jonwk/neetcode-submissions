class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0

        ptr1, ptr2 = 0, 1

        if len(s) <= 1:
            return len(s)
        
        curr = 1
        chars = []
        while ptr1 < ptr2 < len(s):
            maxLen = max(maxLen, curr)
            print(s[ptr1],s[ptr2], curr)
            if s[ptr1] == s[ptr2] and s[ptr1] not in chars:
                chars.add(s[ptr1])
                curr += 1
                ptr2 += 1
            else:
                chars = {}
                ptr1 = ptr2
                ptr2 += 1
                curr = 1
        
        return maxLen

        