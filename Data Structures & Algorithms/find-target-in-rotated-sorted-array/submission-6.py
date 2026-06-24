class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Key: 分 left portion 與 right portion 來做指標移動
        Step 1: 哪半邊是有序的？ → 用 nums[l] <= nums[mid] 判斷（左半有序）
        Step 2: target 在有序的那半邊嗎？ → 在的話就往那邊縮，不在就往另一邊
        """
        #nums = [3,4,5,6,1,2], target = 4
        #nums = [5,1,3], target = 5
        
        l, r = 0, len(nums) - 1        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target: #First Check if it is already Target
                return mid

            if nums[l] <= nums[mid]: #Sorting in the Left Portion (<= 才是都在左界的情況)
                if nums[l] <= target < nums[mid]:  # target 在左半的範圍
                    r = mid - 1
                else: # target 不在左半的範圍
                    l = mid + 1
            else: #nums[l] > nums[mid], Sorting in the Right Portion
                if nums[mid] < target <= nums[r]:  # target 在右半的範圍
                    l = mid + 1
                else: # target 不在右半的範圍
                    r = mid - 1
        return -1



