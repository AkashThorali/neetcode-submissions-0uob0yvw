# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # establish slow and fast pointers

        curr = head
        s = curr
        f = curr.next

        while f and f.next:
            s = s.next
            f = f.next.next

        # reverse second half of linked list
        second = s.next
        s.next = None
        prev = None

        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge two halfs together
        first = head
        second = prev
        while second: 
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            




