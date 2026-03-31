# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
    
        if not head:
            return False

        fast = curr.next
        slow = curr

        while fast and fast.next: 
            if fast is slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False