class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       l = 0
       r = 0

       duplicates = set()
       res = 0

       while r < len(s):
            while s[r] in duplicates:
                duplicates.remove(s[l])
                l += 1
            duplicates.add(s[r])
            res = max(res, len(duplicates))
            r += 1
       return res
        




        
