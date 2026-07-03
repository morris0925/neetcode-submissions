# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Concept: Use Dummy Node to 
        1. prevent from inserting to an empty list
        2. prevent from choosing which one as lead
        """

        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val: # add list1
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return dummy.next





