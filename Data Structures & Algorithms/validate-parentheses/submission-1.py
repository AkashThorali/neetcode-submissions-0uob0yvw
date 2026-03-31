class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        count = {")": "(", "]": "[", "}":"{"}

        for c in s:
            if c in count.values():
                stack.append(c)
            elif c in count:
                if not stack or stack[-1] != count[c]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
        