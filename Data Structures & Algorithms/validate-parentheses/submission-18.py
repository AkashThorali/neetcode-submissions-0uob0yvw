class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(", "]": "[", "}": "{"}

        stack = []
        for i in range(len(s)):
            if s[i] not in brackets.keys(): 
                stack.append(s[i])
            else: 
                if not stack or brackets[s[i]] != stack.pop(): 
                    return False
        return not stack
                