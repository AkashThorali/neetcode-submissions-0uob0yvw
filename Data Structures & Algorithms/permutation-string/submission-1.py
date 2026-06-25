class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0

        if len(s2) < len(s1): 
            return False

        while r < len(s2):
            length = (r - l) + 1
            if length != len(s1): 
                r += 1
            else:
                if sorted(s1) == sorted(s2[l:r+1]): 
                    return True
                l += 1
        return False
