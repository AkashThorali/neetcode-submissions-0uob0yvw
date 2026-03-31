class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        largest = 0
        while l < len(heights):
            r = l
            while r < len(heights):
                distance = r - l
                area = min(heights[l], heights[r]) * distance
                largest = max(largest, area)
                r += 1
            l += 1
        return largest
