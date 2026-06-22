class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums)
        maxLength =  0
        for i in range(len(nums)):
            value = nums[i]
            if value - 1 not in sequence:
                length = 0
                while value + length in sequence:
                    length += 1
                maxLength = max(length, maxLength)
        return maxLength

        