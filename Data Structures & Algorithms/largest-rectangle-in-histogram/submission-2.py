class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Optimal Solution
        Use "Monotonic Stack" to deal with while left and while right tracking
        1. Monotonic increasing: whenever the element comes in, there exists greater in the stk[-1], pop them out, the last element popped out will possess the index that the height can start
        2. When popped out because meeting lower bars, calculate the area and compare with the max
        3. Update that lower bar's start point at the last popped out element, or else the i will be it's max starting point

        Trap:
        a. stack should be storing index and height, compare by height, but alter starting point and record using index
        b. after the for loop, should still calculate the elements' height still in the stack
        """ 

        stk = [] #(index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i #key step to make sure different start pt could be stored
            while stk and h < stk[-1][1]:
                index, height = stk.pop()
                maxArea = max(maxArea, (i - index) * height)
                start = index
            stk.append((start, h)) #not i, h
        
        r = len(heights) - 1
        for i, h in stk:
            maxArea = max(maxArea, (r - i + 1) * h)

        return maxArea


