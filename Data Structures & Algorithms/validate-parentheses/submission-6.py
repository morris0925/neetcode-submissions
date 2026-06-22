class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(", "]":"[", "}":"{"}
        stk = [] #LIFO!


        for e in s:
            #edge case
            if len(s) % 2 == 1:
                return False
            if s[0] in dic:
                return False
            
            if e not in dic:
                stk.append(e)
            else:
                if not stk or stk[-1] != dic[e]: 
                    return False
                else:
                    stk.pop()
        
        return len(stk) == 0 