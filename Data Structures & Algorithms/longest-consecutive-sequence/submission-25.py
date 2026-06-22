class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength =  0
        sequence = set(nums)

        if not nums: 
            return 0
        for i in range(len(nums)):
            count = 0 
            value = nums[i]
            while value + 1 in sequence: 
                count += 1
                value += 1
            maxLength = max(count, maxLength)
        return maxLength + 1

        