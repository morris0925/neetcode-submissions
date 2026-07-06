# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #brute force: use hash sets to record nodes

        wentThru = set()
        curr = head
        while curr:
            if curr in wentThru:
                return True
            else:
                wentThru.add(curr)
                curr = curr.next
        return False
