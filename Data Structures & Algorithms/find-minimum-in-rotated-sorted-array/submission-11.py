class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        smallest = nums[0]
        while l <= r: 
            
            mid = (l + r) // 2
            smallest = min(smallest, nums[mid])
            if nums[l] <= nums[mid]:
                smallest = min(smallest, nums[l])
                l = mid + 1
            else: 
                r = mid - 1
        return smallest
        
                