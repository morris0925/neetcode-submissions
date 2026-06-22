class MinStack:
    #LIFO
    #Key: use a MinStack to store all latest min, in case being popped
    #Correction: Use self.stack 這樣才不是區域變數
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            if val <= self.minStack[-1]: # <= 都要放！
                self.minStack.append(val)
        else:
            self.minStack.append(val)


    def pop(self) -> None:
        pop = self.stack[-1]
        self.stack.pop()
        if pop == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
