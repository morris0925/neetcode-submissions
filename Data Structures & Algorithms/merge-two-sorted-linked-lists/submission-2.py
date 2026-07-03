# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 4
        # 1 3 5
        # Did not use dummy variable: prevent empty list + decide which goes first
        

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

        if list1: #還有剩，直接串下一個上去就好，後面都還是連著
            curr.next = list1

        if list2: 
            curr.next = list2
        
        return head


