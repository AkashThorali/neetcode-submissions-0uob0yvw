class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2
            if nums[m] == target:
                return m

            # nums[m] is in the left portion
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: 
                    r = m - 1

            # nums[m] is in the right portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else: 
                    l = m + 1
        return -1