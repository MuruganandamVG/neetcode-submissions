# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        current=head
        length=0
        while current:
            current=current.next
            length+=1
        target=length-n
        if target==0 and n==1:
            return None
        if target==0 and n>1:
            return head.next
        var=1
        current=head
        while current and current.next:
            if var==target:
                current.next=current.next.next
                break
            current=current.next
            var+=1
        return head
        