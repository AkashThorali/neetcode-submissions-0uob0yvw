import operator as op
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        string1, string2 = {}, {}

        for i in t: 
            string2[i] = 1 + string2.get(i, 0)
        
        have, need = 0, len(string2)
        res = [-1,-1]
        resLen = float("infinity")
        l = 0
        for r in range(len(s)):
            character = s[r]
            string1[character] = 1 + string1.get(character, 0)
            if character in string2 and string1[character] == string2[character]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen: 
                    resLen = r - l + 1
                    res = [l, r]
                remove = s[l]
                string1[remove] -= 1
                if remove in string2 and string1[remove] < string2[remove]:
                    have -= 1
                l += 1
        if resLen == float("infinity"):
            return ""
        else: 
            return s[res[0]:res[1] + 1]



        