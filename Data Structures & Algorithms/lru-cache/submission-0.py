class Node:
    def __init__(self,key,val,prev=None,next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail 
        self.tail.prev=self.head
        self.cache={}
        
        
    def remove_node(self,node):
        prevNode=node.prev
        nextNode=node.next 
        prevNode.next=nextNode
        nextNode.prev=prevNode
    
    def insert_node(self,node):
        prev,next=self.tail.prev,self.tail
        prev.next=next.prev=node 
        node.next,node.prev=next,prev
    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            # delete this node 
            self.remove_node(node)
            # insert at the tail node 
            self.insert_node(node)
            return node.val
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            self.remove_node(node)
            # delete this node 
            
        self.cache[key]=Node(key,value)
        self.insert_node(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.head.next 
            self.remove_node(lru)
            del self.cache[lru.key]
        
       


        
