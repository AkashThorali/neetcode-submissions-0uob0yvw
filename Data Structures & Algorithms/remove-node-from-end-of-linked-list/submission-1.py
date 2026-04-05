# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head

        while n > 0: 
            fast = fast.next
            n -= 1
            if fast is None: 
                print("returned")
                return head.next
        
        prev = None
        while fast: 
            prev = slow
            fast = fast.next
            slow = slow.next
        prev.next = slow.next
        return head
            
