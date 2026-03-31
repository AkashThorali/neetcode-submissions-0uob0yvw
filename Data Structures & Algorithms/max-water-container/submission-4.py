class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxArea = 0
        while l < r: 
            width = r - l 
            length = min(heights[l], heights[r])
            area = length * width
            maxArea = max(maxArea, area)
            if heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1
        return maxArea


            
        