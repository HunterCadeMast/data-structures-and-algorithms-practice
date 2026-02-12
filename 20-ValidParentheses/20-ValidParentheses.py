# Last updated: 2/12/2026, 3:45:44 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')' : '(', ']' : '[', '}' : '{',}
        for character in s:
            if character in pairs.values():
                stack.append(character)
            elif character in pairs:
                if not stack or stack[-1] != pairs[character]:
                    return False
                stack.pop()
            else:
                return False
        return not stack