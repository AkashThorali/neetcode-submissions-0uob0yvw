# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        condense = []
        for head in lists:
            curr = head
            while curr:
                condense.append(curr.val)
                curr = curr.next 

        condense.sort()
        
        dummy = ListNode()
        curr = dummy

        for i in condense: 
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
        

                 
