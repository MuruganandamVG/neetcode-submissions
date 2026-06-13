# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack=[]
        current=head
        while current:
            stack.append(current)
            current=current.next 
        var=head
        while stack:
            var.next=stack.pop(0)
            var=var.next
            if stack:
                var.next=stack.pop()
                var=var.next 
        var.next=None


        