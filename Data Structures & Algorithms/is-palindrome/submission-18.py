class Solution:
    def isPalindrome(self, s: str) -> bool:
        formattedStr = ''.join([c.lower() for c in s if c.isalnum()])

        left, right = 0, len(formattedStr) - 1
        
        while left < right:
            if formattedStr[left] != formattedStr[right]:
                    return False
            left += 1
            right -= 1
            
        return True