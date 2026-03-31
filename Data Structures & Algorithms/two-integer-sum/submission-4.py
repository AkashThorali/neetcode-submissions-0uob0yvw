class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for index, number in enumerate(nums): 
            diff = target - number
            if diff in res: 
                return [res[diff], index]
            res[number] = index
        return []
