class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Fact: 
        if L[-1] is greater than L[0] (rotated), start from the middle and see which direction to go
        if L[0] is smaller than L[-1], L[0] is the smallest
        """
        # [3,4,5,6,1,2]

        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
                return nums[l]
        else:
            minN = min(nums[l], nums[r])
            while l <= r:
                mid = (l+r)//2
                if nums[mid] < minN:
                    r = mid - 1
                    minN = min(nums[mid], nums[r])
                else:
                    l = mid + 1
            return minN


