# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        prev = newHead
        curr1 = list1
        curr2 = list2

        while curr1 and curr2: 
            if curr1.val > curr2.val:
                prev.next = curr2
                curr2 = curr2.next
            else:
                prev.next = curr1
                curr1 = curr1.next
            prev = prev.next
        
        if not curr1: 
            prev.next = curr2
        elif not curr2: 
            prev.next = curr1

        return newHead.next
        