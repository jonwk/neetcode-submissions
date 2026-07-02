class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char not in close_to_open:
                stack.append(char)
            else:
                # starting with a closed bracket
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != close_to_open[char]:
                        return False
        
        return len(stack) == 0
                    

        