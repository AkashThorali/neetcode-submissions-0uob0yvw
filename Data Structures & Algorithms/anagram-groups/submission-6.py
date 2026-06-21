from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs: 
            anagram = [0] * 26
            for letter in word:
                anagram[ord(letter) - ord('a')] += 1
            res[tuple(anagram)].append(word)
        return list(res.values())


            


