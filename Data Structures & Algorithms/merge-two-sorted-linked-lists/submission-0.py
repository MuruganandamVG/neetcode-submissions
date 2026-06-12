# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        dummyNode=ListNode()
        curr=dummyNode
        while(temp1 is not None and temp2 is not None):
            if (temp1.val<=temp2.val):
                curr.next=ListNode(temp1.val)
                temp1=temp1.next
            else:
                curr.next=ListNode(temp2.val)
                temp2=temp2.next 
            curr=curr.next
        while(temp1 is not None):
                curr.next=ListNode(temp1.val)
                temp1=temp1.next
                curr=curr.next
        while(temp2 is not None):
                curr.next=ListNode(temp2.val)
                temp2=temp2.next
                curr=curr.next
        return dummyNode.next
        