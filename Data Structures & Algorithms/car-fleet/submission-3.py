class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Pretty Hard: Need to know the answer (Single Solution)
        1. Look backwards from starting point, see if the second one requires less time than first one to arrive at destination.
        2. Use monotonic increasing stack to store the fleet, any smaller time will be eliminated as it becomes fleet with existing one.
        3. Physics: Use time to destination to evaluate whether collide.
        """

        cars = list(zip(position, speed))
        cars.sort(reverse=True) #遞減
        stk = [] #放t
        for p, s in cars:
            t = (target - p) / s
            if stk and t <= stk[-1]: #不需要刪除東西
                continue
            else:
                stk.append(t)
        
        return len(stk)

                






        