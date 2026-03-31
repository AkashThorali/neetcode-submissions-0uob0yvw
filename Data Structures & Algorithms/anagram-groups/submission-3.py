class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs: 
            sorted_string = tuple(sorted(i))
            if sorted_string in res:
                res[sorted_string].append(i)
            else: 
                res[sorted_string] = [i]
        return list(res.values())