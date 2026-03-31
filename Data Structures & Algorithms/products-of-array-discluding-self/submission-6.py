class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first pass (prefix)
        # nums: [1,2,4,6]
        # res: [1,1,2,8]
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # second past (postfix)
        # nums: [1,2,4,6]
        # res: [48,24,12,8]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        

