class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSet = set()
        count = 0
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in longestSet:
                longestSet.remove(s[l])
                l += 1
            longestSet.add(s[r])
            res = max(res, r - l + 1)
        return res


