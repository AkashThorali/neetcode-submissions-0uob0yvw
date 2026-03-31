class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 

            m = (l + r) // 2
            if nums[l] == target: 
                return l
            elif nums[r] == target: 
                return r
            elif nums[m] == target: 
                 return m
            else: 

                # bigger portion
                if nums[m] >= nums[l]: 
                    if nums[m] >= target and target >= nums[l]:
                        r = m
                    else: 
                        l = m + 1
                else: 
                    if target >= nums[m] and target <= nums[r]:
                        l = m
                    else: 
                        r = m - 1
        return -1

                    