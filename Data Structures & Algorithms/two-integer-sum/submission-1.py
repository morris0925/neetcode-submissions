class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        temp = 0
        for i, num in enumerate(nums):
            temp = target - num
            #不要先建 dictionary
            #確保是往後loop之後回來看 前面相加能否 reach target
            if temp in dic:
                return [dic[temp],i]
            else:
                dic[num] = i
                temp = 0
        
        return []

        