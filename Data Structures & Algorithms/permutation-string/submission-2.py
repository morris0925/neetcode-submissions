class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        for e in s1:
            dic[e] = dic.get(e,0) + 1
        
        check = {}
        win = len(s1)
        #edge case: s1比 s2長則不proceed
        if win > len(s2):
            return False
        
        for i in range(win):
            check[s2[i]] = check.get(s2[i],0) + 1
        
        if check == dic:
            return True

        for i in range(win,len(s2)):
            # remove left
            check[s2[i - win]] -= 1
            if check[s2[i - win]] == 0:
                del check[s2[i - win]]
            # add right
            check[s2[i]] = check.get(s2[i],0) + 1
            if check == dic:
                return True
        
        return False
        













        