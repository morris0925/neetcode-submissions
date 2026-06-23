class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Fact: 
        if L[-1] is greater than L[0] (rotated), start from the middle and see which direction to go
        if L[0] is smaller than L[-1], L[0] is the smallest
        """
        # [4,5,0,1,2,3]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[r]

