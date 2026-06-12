# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        fast=head 
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head 
        slow=head
        while(n):
            fast=fast.next
            n-=1
        if (fast==None):
            return head.next 
        while(fast is not None and fast.next is not None):
            fast=fast.next 
            slow=slow.next 
        slow.next=slow.next.next
        return head
        
        
        while(n):
            fast=fast.next
            n-=1
        while(fast is not None and fast.next is not None):
            fast=fast.next 
            slow=slow.next 
        slow.next=slow.next.next
        return head
        
        