class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1

        res = nums[0]

        while l <= r: 

            # handles case where array is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])

            midpoint = (l + r) // 2
            res = min(res, nums[midpoint])
            # bigger portion
            if nums[midpoint] >= nums[l]:
                l = midpoint + 1
            else:
                r = midpoint - 1
        return res

            

            
