class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        brute force: O(n^2) to loop through all possibilities of each's height, extending left and right
        """
        result = 0
        for i, h in enumerate(heights):
            l = r = i
            #move l: l-1 within range and h is higher
            while l - 1 >= 0 and h <= heights[l-1]:
                l -= 1
            #move r: h is higher and r <= last element
            while r + 1 < len(heights) and h <= heights[r+1]:
                r += 1
            result = max(result, (r-l+1)*h)
        
        return result








        