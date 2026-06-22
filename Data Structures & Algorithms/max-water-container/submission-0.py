class Solution:
    def maxArea(self, heights: List[int]) -> int:
        MaxArea = 0
        for i in range(len(heights)-1, 0, -1): #interval
            l, r = 0, i
            for j in range(len(heights)-i):
                Area = i * min(heights[l],heights[r])
                if Area > MaxArea: 
                    MaxArea = Area
                l += 1
                r += 1
        
        return MaxArea
                
