# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        length=0;
        while(temp):
            temp=temp.next
            length+=1
        if n==length:
            return head.next
        removeIndex=length-n;
        temp=head
        for _ in range(removeIndex-1):
            temp=temp.next
        temp.next=temp.next.next
        return head
        
        