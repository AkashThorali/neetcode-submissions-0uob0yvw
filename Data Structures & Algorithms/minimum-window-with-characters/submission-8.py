class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_valid():
            for char, count in t_dict.items():
                if s_dict.get(char, 0) < count:
                    return False
            return True
            
        if len(s) < len(t):
            return ""

        # is_subset = dict1.items() >= dict2.items()

        s_dict = {}
        t_dict = {}

        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1
        print(t_dict)

        l, r = 0, 0
        length = float('inf')
        shortest = ""
        while r < len(s):
            s_dict[s[r]] = s_dict.get(s[r], 0) + 1
            while is_valid():
                substring = s[l:r + 1]
                print(substring)
                if len(substring) < length: 
                    length = len(substring)
                    shortest = substring
                s_dict[s[l]] -= 1
                if s_dict[s[l]] == 0:
                    s_dict.pop(s[l])
                l += 1 
            r += 1
        return shortest


