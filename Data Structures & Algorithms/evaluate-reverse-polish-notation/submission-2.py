class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for e in tokens:
            if e == "+":
                stack.append(stack.pop() + stack.pop()) #pop()會回傳值！
            elif e == "-":
                a, b = stack.pop(), stack.pop() # 靠近後面的是a, 靠近頭的是b
                stack.append(b - a)
            elif e == "*":
                stack.append(stack.pop() * stack.pop())
            elif e == "/":
                a, b = stack.pop(), stack.pop() # 靠近後面的是a, 靠近頭的是b
                stack.append(int(b / a)) #b//a 會四捨五入不是無條件取整
            else:
                stack.append(int(e))
            
        if stack:
            return stack[0]

        
        
        