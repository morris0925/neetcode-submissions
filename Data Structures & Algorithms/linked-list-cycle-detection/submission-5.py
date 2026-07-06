# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Optimal: Tortoise and Hare approach, space O(1)
        slow, fast = head, head

        while fast and fast.next: #如果都不是 None, 就能有 fast.next.next
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
