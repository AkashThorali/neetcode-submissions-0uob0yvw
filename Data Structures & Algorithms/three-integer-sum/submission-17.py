class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)
        seen = set()
        for i in range(len(nums) - 1): 
            number = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = number + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1 
                else: 
                    triple = [number, nums[left], nums[right]]
                    if tuple(triple) not in seen:
                        res.append(triple)
                        seen.add(tuple(triple))
                    left += 1
                    right -= 1
        return res
        
        

            

            


