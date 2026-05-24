class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')' : '(', '}' : '{',']' : '['}
        stack = []
        
        for c in s:
            if c in bracket_map and stack:
                if bracket_map[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return True if not stack else False