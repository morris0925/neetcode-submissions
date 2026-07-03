# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 4
        # 1 3 5

        """
        Concept: Use Dummy Node to 
        1. prevent from inserting to an empty list
        2. prevent from choosing which one as lead
        """

        if not list1:
            return list2
        if not list2:
            return list1

        
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next

        curr = head

        while list1 and list2:
            if list1.val <= list2.val: #比較下一個元素該取誰
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        if list1: #還有剩，直接串到後面
            while list1:
                curr.next = list1
                curr = list1
                list1 = list1.next        

        if list2: 
            while list2:
                curr.next = list2
                curr = list2
                list2 = list2.next 
        
        return head


