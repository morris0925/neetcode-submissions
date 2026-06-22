class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #idea1: sort first, then append consecutive num to [], pick greatest
        #idea1 rejected since sorted = o(nlogn)

        """Sol: 
        - Use Sets and see if a number has a left neighbor in list
        - A sequence is built when it has no left neighbor
        - Calculate all the sequences and pick the longest sequence"""
        
        numSet = set(nums)
        LongestSeq = 0
        for num in nums:
            if num - 1 not in numSet: #有效排除中間的重跑
                length = 1
                while (num + length) in numSet: #length 算幾個連續
                    length += 1
                LongestSeq = max(LongestSeq, length)

        return LongestSeq    



