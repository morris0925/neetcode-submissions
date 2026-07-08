# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        from collections import deque
        num1 = deque()
        num2 = deque()

        curr1 = l1
        curr2 = l2
        while curr1:
            num1.appendleft(str(curr1.val))
            curr1 = curr1.next
        while curr2:
            num2.appendleft(str(curr2.val))
            curr2 = curr2.next 
        
        num1 = int("".join(num1))
        num2 = int("".join(num2))
        result = str(num1 + num2)
        
        prev = None
        for c in result:
            node = ListNode(int(c))
            node.next = prev
            prev = node
        
        return prev



        

