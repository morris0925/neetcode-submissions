class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #s="pwwkew"
        maxSeq = 0
        seq = 0
        d = set()
        pt = 0 #remove pointer

        for i in range(len(s)): #一定要用s[i]因為這樣才能照順序刪
            if s[i] in d:
                while s[i] in d:
                    d.remove(s[pt])
                    pt += 1 #往下一個刪
                    seq -= 1
                d.add(s[i])
                seq += 1
                maxSeq = max(maxSeq, seq)
                
            else:
                d.add(s[i])
                seq += 1
                maxSeq = max(maxSeq, seq)
        
        return maxSeq



