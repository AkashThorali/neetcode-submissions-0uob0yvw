class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        getDuplicate = set()
        for i in range(len(nums)):
            if nums[i] in getDuplicate:
                return True
            getDuplicate.add(nums[i])

        return False
        
         