class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        MaxArea = 0
        l, r = 0, len(heights) - 1

        # 同時移動的邏輯：找兩個之中小的移動
        while l < r:
            Area = (r-l) * min(heights[l], heights[r])
            if Area > MaxArea:
                MaxArea = Area

            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else: # 無論如何都會停在最大的地方
                l += 1

        return MaxArea


