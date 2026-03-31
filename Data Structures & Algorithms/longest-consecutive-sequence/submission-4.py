class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in nums:

            # checks to see if the number has a left neighbor
            # if not we know it is the start of a sequence
            if (i - 1 not in nums):
                length = 0

                # while there is a number greater than 1 in the set keep adding to length of the seqeunce
                while (i + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        # if len(nums) == 0: 
        #     return 0

        # nums.sort()
        # count = 1
        # longest = 0
        # for i in range(len(nums) - 1):
        #     if (nums[i + 1] - nums[i] == 1):
        #         count += 1
        #     elif(nums[i + 1] == nums[i]):
        #         count += 0
        #     else:
        #         longest = max(count, longest)
        #         count = 1
        # return max(longest, count)


            
        