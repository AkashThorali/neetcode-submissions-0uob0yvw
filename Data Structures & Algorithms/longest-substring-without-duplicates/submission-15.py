class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l = 0
        r = 0

        longest = 0
        while r < len(s):
            if s[r] not in seen: 
                seen.add(s[r])
                r += 1
                longest = max(longest, len(seen))
            else:
                while s[r] in seen: 
                    seen.discard(s[l])
                    l += 1
        return longest


