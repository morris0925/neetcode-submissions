# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Official Solution: add up with a "carry"(進位) consideration
        Note: Lots of edge cases - be mindful to look at if there's carry in the end
        """

        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            res = val1 + val2 + carry

            oneth = res % 10
            carry = res // 10
            node = ListNode(oneth)
            curr.next = node
            curr = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
            
            







        