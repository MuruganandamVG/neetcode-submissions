# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1,list2):
            temp1=list1
            temp2=list2
            dummyNode=ListNode(-1)
            dummy=dummyNode
            while( temp1 is not None and temp2 is not None):
                if(temp1.val<=temp2.val):
                    dummy.next=temp1
                    dummy=dummy.next 
                    temp1=temp1.next
                else:
                    dummy.next=temp2
                    dummy=dummy.next
                    temp2=temp2.next 
            if temp1 is not None:
                dummy.next=temp1
            if temp2 is not None:
                dummy.next=temp2
            return dummyNode.next 
        n=len(lists)
        if not lists:
            return None
        def mergelists(index):
            if(index==n-1 or lists[index] is None):
                return lists[index]
            mergeHead=mergelists(index+1)
            return merge(lists[index],mergeHead)
        return mergelists(0)
        
        