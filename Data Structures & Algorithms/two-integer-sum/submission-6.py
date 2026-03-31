from collections import Counter


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = {}
        for index in range(len(nums)):
            difference = target - nums[index]
            if difference in res: 
                return [res[difference], index]
            else: 
                res[nums[index]] = index

        