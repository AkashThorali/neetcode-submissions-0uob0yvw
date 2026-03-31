class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for word in strs: 
            encode += str(len(word)) + "#" + word
        return encode


    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            delimiter = i
            while s[delimiter] != "#":
                delimiter += 1
            
            length = int(s[i:delimiter])
            i = delimiter + 1
            res.append(s[i: i + length])
            i += length
        return res



