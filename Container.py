class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        area = 0
        count = 0
        while l < r:
            if heights[l] < heights[r]:
                if area < heights[l]*(len(heights)-count-1):
                    area = heights[l]*(len(heights)-count-1)
                l += 1
                count += 1
            else:
                if area < heights[r]*(len(heights)-count-1):
                    area = heights[r]*(len(heights)-count-1)
                r -= 1
                count += 1
        return area
