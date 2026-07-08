class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return n
            else:
                hashSet.add(n)
    