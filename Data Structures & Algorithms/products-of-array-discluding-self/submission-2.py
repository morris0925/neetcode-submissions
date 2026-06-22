class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums) #[1    , 1  , 1*2, 1*2*4]
        suffix = [1] * len(nums) #[2*4*6, 4*6, 6  , 1    ]
        result = []

        pre = 1
        suf = 1
        for i in range(len(nums)-1):
            pre = pre * nums[i]
            prefix[i+1] = pre

            suf = suf * nums[len(nums)-1-i]
            suffix[len(nums)-2-i] = suf

        for i in range(len(nums)):
            product = prefix[i] * suffix[i]
            result.append(product)
        
        return result

#Learnings: Python 沒有 prepend，取而代之用 [1]*n 先建好，再來修改其中元素～

        