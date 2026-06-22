class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #"AABBABB", k=2
        # char to be replaced: window_size - dic[max_char] <= k

        # maxCharCnt = max(dic.values()) 
        #學起來：dic.value() 會 return dic_values[1.3.4.2]
        #這是一個 "View Object"，不是list但可以被 max()、sum()、for、list()
        #但注意 max(空) 會報錯

        dic = {}
        winSize = 0
        maxSize = 0
        ptr = 0 #track where window starts
        
        for i in range(0, len(s)):
            dic[s[i]] = dic.get(s[i],0) + 1
            maxCharCnt = max(dic.values()) 
            winSize += 1
            
            if winSize - maxCharCnt <= k:
                if winSize > maxSize:
                    maxSize = winSize
            
            else:
                while winSize - maxCharCnt > k:
                    dic[s[ptr]] -= 1
                    if dic[s[ptr]] == 0:
                        del dic[s[ptr]]
                    winSize -= 1
                    ptr += 1

        return maxSize


        













        