class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # have a left pointer at the beginning and right at the end
        # have an element be the distance between the elements
        # find the minimum element and then multiply that by the distance between the elements
        # have a maximum variable to keep track of heights
        # keep decrementing the right pointer until it at the left, then reset and move the left pointer up by 1
        
        
        max_water = 0
        for index in range(len(heights) - 1): 
            l = index
            r = len(heights) - 1
            distance = r - index

            while l < r:
                container = min(heights[l], heights[r]) * distance
                print(f"Multiplying min({heights[l]}, {heights[r]}) = {min(heights[l], heights[r])} by distance {r - l} → {container}")
                max_water = max(max_water, container)
                r -= 1
                distance -= 1
        return max_water
            