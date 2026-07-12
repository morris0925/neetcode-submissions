"""
1. use dictionary to store key with node address
2. node.val to store value
3. use doubly linked list to alter nodes used, add and eliminate
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            self.remove(self.dic[key]) # remove from linked list
            self.insert_to_head(self.dic[key]) # add to linked list
            return self.dic[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].val = value
            self.remove(self.dic[key]) # remove from linked list
            self.insert_to_head(self.dic[key]) # add to linked list
            return
        
        if len(self.dic) >= self.cap:
            del self.dic[self.tail.prev.key] #remove from dictionary (should be done first, ref tail.prev)
            self.remove(self.tail.prev) #remove tail.prev
            self.dic[key] = Node(key,value)
            self.insert_to_head(self.dic[key]) #insert to head
        else:
            self.dic[key] = Node(key,value)
            self.insert_to_head(self.dic[key]) #insert to head

    def remove(self, node):
        nxt = node.next
        prev = node.prev
        nxt.prev = prev
        prev.next = nxt

    def insert_to_head(self, node):
        nxt = self.head.next
        self.head.next = node
        node.next = nxt
        nxt.prev = node
        node.prev = self.head





