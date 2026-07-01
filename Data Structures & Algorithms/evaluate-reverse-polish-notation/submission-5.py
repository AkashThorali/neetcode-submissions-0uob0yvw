class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        stack = []
        for element in tokens: 
            if element in operators: 
                first = stack.pop()
                second = stack.pop()
                if element == "+": 
                    stack.append(second + first)
                elif element == "-":
                    stack.append(second - first)
                elif element == "*":
                    stack.append(second * first)
                else: 
                    stack.append(int(second / first))
            else: 
                stack.append(int(element))
        return stack.pop()
