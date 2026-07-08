"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Optimal Sol:
        1. Note down the address pairing new copy
        2. Connect them and pair the random link
        """
        
        hashMap = {None:None} #null:null 要放進去，因為最後沒辦法加
        curr = head
        while curr:
            copy = Node(curr.val)
            hashMap[curr] = copy
            curr = curr.next
        # still missing None in the end

        curr = head
        while curr:
            node = hashMap[curr]
            node.next = hashMap[curr.next]
            node.random = hashMap[curr.random]
            curr = curr.next

        return hashMap[head]
        


