class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        
        maxLength = 0
        for i in nums: 
            count = 1
            while i + 1 in res: 
                count += 1
                i += 1
            maxLength = max(maxLength, count)
        return maxLength

        