class Solution:
    def isValid(self, s: str) -> bool:
        # ord 之間可不一定都只差 1!
        # 用 dic 可以把 '{' 配對 '}'

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
                if not stk: #如果stack裡面是空的卻遇到close bracket
                    return False
                if stk[-1] == dic[e]:
                    stk.pop()
                else:
                    return False
        if stk:
            return False
        else:
            return True