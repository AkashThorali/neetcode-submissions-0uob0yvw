class Solution:
    def isValid(self, s: str) -> bool:

        table = {')':'(','}':'{',']':'[' }
        stack = []

        for i in s: 

            if i in table.values(): 
                stack.append(i)
            elif stack: 
                element = stack.pop()
                if table[i] != element:
                    return False
            else: 
                return False
        if not stack: 
            return True
        else: 
            return False
        