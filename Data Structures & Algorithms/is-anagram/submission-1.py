class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for element in s:
            if element not in dic:
                dic[element] = 1
            else:
                dic[element] += 1

        for element in t:
            if element not in dic:
                return False
            else:
                dic[element] -= 1
        
        for val in dic.values():
            if val != 0:
                return False
        return True