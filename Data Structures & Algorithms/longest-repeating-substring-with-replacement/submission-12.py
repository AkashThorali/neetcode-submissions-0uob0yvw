class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        
        frequency = {}
        longest = 0
        for r in range(len(s)):
            frequency[s[r]] = 1 + frequency.get(s[r], 0)

            length = (r-l) + 1
            if length - max(frequency.values()) > k:
                frequency[s[l]] -= 1
                l += 1
            longest = max(longest, (r-l) + 1)
        return longest

            




        
        
                    


                
            

                