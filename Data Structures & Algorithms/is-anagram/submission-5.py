class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordOne = {}
        wordTwo = {}

        for i in s: 
            wordOne[i] = wordOne.get(i, 0) + 1

        for i in t: 
            if i in wordTwo:
                wordTwo[i] += 1
            else: 
                wordTwo[i] = 1
        return wordOne == wordTwo