"""
1. Use Dictionary to search key with value for O(1), but dictionary alone cannot implement from the least recent to most recent.
2.1 If the value wants to be sorted, use "array" or "list", make head the most recent while tail the least recent, to squeeze out LRU in O(1).
2.2 But since we might be picking from the middle with O(1), use doubly linked list and use dictionary to help us get the location
"""    
class Node:
    def __init__(self, key, val): #key 需要因為 put function 要用到 del dic[self.tail.prev.key]
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:  

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.head = Node(0,0) #dummy node 為了讓中間元素串接
        self.tail = Node(0,0) #dummy node 為了讓中間元素串接
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            self.remove(self.dic[key]) # pull the node dic[key]
            self.insert_in_front(self.dic[key]) # add to the front
            return self.dic[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        #edge case: if key in dic but wanna change value
        if key in self.dic:
            self.dic[key].val = value
            self.remove(self.dic[key])
            self.insert_in_front(self.dic[key])
            return  #沒有 return 就有可能繼續跑進去 delete LRU!!

        #delete the LRU if full
        if len(self.dic) >= self.cap:
            del self.dic[self.tail.prev.key]  #delete dic[key]
            self.remove(self.tail.prev) #pull the node at the end，這個不能先delete因為dic會沒有reference可以刪除
            self.dic[key] = Node(key, value)
            self.insert_in_front(self.dic[key]) #insert the node in the beginning
        else:
            self.dic[key] = Node(key, value)
            self.insert_in_front(self.dic[key]) #insert the node in the beginning

    def remove(self, node):
        nxt = node.next
        prev = node.prev
        nxt.prev = prev
        prev.next = nxt
    
    def insert_in_front(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head


