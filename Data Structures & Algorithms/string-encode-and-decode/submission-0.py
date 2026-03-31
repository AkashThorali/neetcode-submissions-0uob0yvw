class Solution:

    def encode(self, strs: List[str]) -> str:
        decode = ""
        for i in strs:
            decode += str(len(i)) + "#" + i
        return decode


    def decode(self, s: str) -> List[str]:
        result = []
        count = 0

        while count < len(s):
            index = count
            while s[index] != "#":
                index += 1
            length = int(s[count:index])
            result.append(s[index + 1: index + 1 + length])
            count = index + 1 + length
        return result



