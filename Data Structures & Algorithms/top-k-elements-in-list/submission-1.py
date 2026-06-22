class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse = True)
        
        result = []
        for x in sorted_dic[:k]:
            result.append(x[0])
        
        return result
        