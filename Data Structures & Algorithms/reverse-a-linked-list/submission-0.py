# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        res=[]
        while(temp is not None):
            res.append(temp.val)
            temp=temp.next
        res.reverse()
        dummyNode=ListNode()
        curr=dummyNode
        for i in range(len(res)):
            curr.next=ListNode(res[i])
            curr=curr.next
        return dummyNode.next
        