class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        currSum = 0

        for number in nums: 
            if currSum < 0:
                currSum = 0
            currSum += number
            maximum = max(maximum, currSum)
        return maximum