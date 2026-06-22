class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sorted_nums = sorted(nums)
        duplicates = set()

        for i in range(len(nums)):
            if sorted_nums[i] in duplicates:
                continue
            duplicates.add(sorted_nums[i])
            value = sorted_nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if sorted_nums[l] + value + sorted_nums[r] > 0:
                    r -= 1
                elif sorted_nums[l] + value + sorted_nums[r] < 0:
                    l += 1
                else: 
                    res.append([sorted_nums[l], value, sorted_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l-1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r+1]:
                        r -= 1
        return res
            

            

            

            


