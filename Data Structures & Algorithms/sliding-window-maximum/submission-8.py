class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Solution: Monotonic Decreasing Queue
        Correction from prev attempt: queue stores indices, to make it monotonic decreasing in value, and meanwhile being able to count if it's out of window size
        """
        from collections import deque
        maxq = deque()
        result = []

        for i in range(len(nums)):
            while maxq:
                # monotonic decreasing
                if nums[i] > nums[maxq[-1]]:
                    maxq.pop()
                else:
                    break
            maxq.append(i)

            # check window size
            if i - maxq[0] == k:
                maxq.popleft()

            # start recording when reached window size
            if i + 1 >= k: 
                result.append(nums[maxq[0]])
            
        return result





