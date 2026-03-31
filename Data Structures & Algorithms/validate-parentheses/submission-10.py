class Solution:
    def isValid(self, s: str) -> bool:
        characters = {')': '(', '}':'{', ']':'['}

        stack = []
        for symbol in s:
            if symbol in characters.values():
                stack.append(symbol)
            else: 
                if not stack or characters[symbol] != stack.pop(): 
                    return False
        
        return False if stack else True
                