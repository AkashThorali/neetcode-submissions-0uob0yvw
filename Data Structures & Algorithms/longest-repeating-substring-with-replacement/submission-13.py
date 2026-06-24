class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        longest = 0

        freq = {}
        while r < len(s):
            if s[r] in freq: 
                freq[s[r]] += 1
            else: 
                freq[s[r]] = 1
            
            length = (r - l) + 1
            while length - max(freq.values()) > k: 
                freq[s[l]] -= 1
                length -= 1
                l += 1
            longest = max(longest, length)
            r += 1
        return longest


            




        
        
                    


                
            

                