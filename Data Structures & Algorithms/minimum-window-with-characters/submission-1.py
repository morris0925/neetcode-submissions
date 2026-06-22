class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        HAVEcnt vs NEEDcnt: when A count == A needed, 
        HAVEcnt + 1 and leave it, no matter if more are met
        until HAVEcnt == NEEDcnt, we know we got all elements needed
        '''

        have = {}
        need = {}

        for e in t:
            need[e] = need.get(e,0) + 1

        HaveCnt = 0
        NeedCnt = len(need)
        
        minCount = len(s) + 1
        minL = 0
        minR = 0
        l = 0
        for r in range(len(s)): # r for right
            if s[r] in need:
                have[s[r]] = have.get(s[r], 0) + 1
                if have[s[r]] == need[s[r]]: #meeting minimum demand
                    HaveCnt += 1
            
            while HaveCnt == NeedCnt: #只有HaveCnt == NeedCnt會不斷符合
                if r - l + 1 < minCount:
                    minCount = r - l + 1
                    minL = l
                    minR = r
                    
                if s[l] in have:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        HaveCnt -= 1
                l += 1
        if minCount == len(s) + 1:
            return ""
        else:
            return s[minL:minR+1]




            


