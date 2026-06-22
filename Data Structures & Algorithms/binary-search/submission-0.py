class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Split from the middle each time and move toward left or right to approach it
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            midIndex = (l + r) // 2
            if target > nums[midIndex]:
                l = midIndex + 1 #加一很關鍵！檢查過不是就要排除
            elif target == nums[midIndex]:
                return midIndex
            else:
                r = midIndex - 1 
        return -1