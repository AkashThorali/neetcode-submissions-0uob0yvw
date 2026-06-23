class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        duplicates = set()

        nums = sorted(nums)
        for i in range(len(nums)):

            # avoids redudancy
            if nums[i] in duplicates: 
                continue
            duplicates.add(nums[i])

            l = i + 1
            r = len(nums) - 1
            while l < r: 
                if nums[l] + nums[i] + nums[r] < 0: 
                    l += 1
                elif nums[l] + nums[i] + nums[r] > 0: 
                    r -= 1
                else: 
                    res.append([nums[l], nums[i], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res



            

            

            

            


