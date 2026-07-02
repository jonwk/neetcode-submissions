class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        formatted_s = ""
        for char in s:
            if char.isalnum():
                formatted_s += char.lower()
    
        left, right = 0, len(formatted_s)-1
        while left <= right:
            if formatted_s[left] != formatted_s[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True