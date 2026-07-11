class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ Solution that is not intuitive...
        1. recognize as linked list cycle
        2. use Floyd's algorithm: fast and slow will met, once meet, set another starter from zero to go, they will meet directly at "cycle start"
        
        AKA "meeting pt" to "cycle start" == "0" - "cycle start"
        proof: 2(s + c - x) = s + c + (c - x) => x = s
        """

        slow, fast = 0, 0
        while True:
            s_next = nums[slow]
            f_next = nums[nums[fast]]
            slow = s_next
            fast = f_next
            if slow == fast:
                break
        
        ptr = 0
        while True:
            ptr_next = nums[ptr]
            s_next = nums[slow]
            ptr = ptr_next
            slow = s_next
            if ptr == slow:
                return ptr
    


