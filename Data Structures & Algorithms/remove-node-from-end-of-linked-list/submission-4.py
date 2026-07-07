# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Optimal: first create the gap - 1 and move forward till the end
        """

        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head #temporary

        while n > 0 and right:
            right = right.next
            n -= 1
        
        # already an n+1 gap
        # move till the end
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next








