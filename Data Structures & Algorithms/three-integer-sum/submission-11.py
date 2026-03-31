class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        sortedNums = sorted(nums)

        for i, a in enumerate(sortedNums):
            if a > 0: 
                break
        
            if i > 0 and a == sortedNums[i - 1]:
                continue

            l = i + 1
            r = len(sortedNums) - 1
            while l < r: 
                threeSum = a + sortedNums[l] + sortedNums[r]
                if threeSum < 0: 
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else: 
                    res.append([a, sortedNums[l], sortedNums[r]])
                    l += 1
                    r -= 1
                    while sortedNums[l] == sortedNums[l -1] and l < r: 
                        l += 1
        return res

            


