class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, A in enumerate(nums):
            
            if i > 0 and A == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            
            # [-4,-1,-1,0,1,2]
            while l < r:
                if A + nums[l] + nums[r] == 0: #關鍵：選定數字右邊開始跑指針
                    result.append([A,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    
                    #不重複關鍵：注意若前後移了一樣要再跳一格，條件難！
                    while nums[l-1] == nums[l] and l<r:
                        l += 1
                    while nums[r+1] == nums[r] and l<r:
                        r -= 1
                    
                    
                elif A + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        
        return result

