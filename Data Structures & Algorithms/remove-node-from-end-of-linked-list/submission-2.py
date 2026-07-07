# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1,2,3,4] n=2

        slow, fast = head, head
        cnt = 0

        while fast:
            fast = fast.next
            cnt += 1
        
        target = cnt - n
        
        if target == 0:
            head = head.next
        else:
            while target > 1:
                slow = slow.next
                target -= 1
            slow.next = slow.next.next

        return head
