class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        When you need "Next Greater/Smaller Element"
        or "Previous Greater/Smaller Element"
        => MONOTONIC STACK to achieve O(n) finding next greater or smaller element
        """
        #works for daily temp, trapping rain...

        """
        Logic: A stack storing monotonic decreasing number, if bigger, pop the small ones
        Use tuples to save not only number, but also sequence
        Update result by first setting to [0] * n
        stk = [[38,1],[30,2],[36,3],[35,4],[40,5],[28,6]]
        result = [0,0,0,0,0,0,0]
        """


        stk = [] #monotonic decreasing stack
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][0]: #當stk內有東西，且比最上面那個的值大
                t_temp, t_seq = stk.pop()
                result[t_seq] = i - t_seq
            stk.append([t,i])
        
        return result




        
        