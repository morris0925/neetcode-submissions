# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Brute Force: make a reverse linked list O(n) space
        #create result, 完全覆蓋掉原來 head 結構 

        curr = head
        prev = None
        count = 0
        while curr:
            node = ListNode(curr.val)
            node.next = prev
            prev = node
            curr = curr.next
            count += 1
        
        dummy = ListNode()
        result = dummy
        for i in range(count):
            if i % 2 == 0:
                result.next = head
                head = head.next
            else:
                result.next = node
                node = node.next
            result = result.next
        
        result.next = None
        

        