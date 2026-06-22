class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 0 

        l_max = [] # 用夾的
        r_max = []
        # [0,2,2,3,3,3,3,3,3]
        # [3,3,3,3,3,3,3,2,1]

        for i in range(len(height)):
            if height[i] > l:
                l = height[i]
                l_max.append(l)
            else:
                l_max.append(l)
            
            if height[len(height) - i - 1] > r:
                r = height[len(height) - i - 1]
                r_max.append(r) #note: 應該要prepend但我們最後再反過來！
            else:
                r_max.append(r)

            i += 1
        r_max.reverse() #不然順序會是最右邊的值在 r_max[0]

        result = 0
        for i in range(len(height)):
            result += min(l_max[i], r_max[i]) - height[i]

        return result    


        