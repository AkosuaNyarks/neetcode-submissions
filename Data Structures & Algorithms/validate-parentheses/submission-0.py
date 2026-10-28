class Solution:
    def isValid(self, s: str) -> bool:
        match={")":"(","}":"{","]":"["}
        stack=[]
        for char in s:
            if char not in match:
                stack.append(char)
            elif char  in match and stack and match[char]==stack[-1]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
        