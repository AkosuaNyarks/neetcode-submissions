# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        #1. Split the Linked List into using slow and fast pointers
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        # reverse the second half of the linked list
        second=slow.next
        slow.next=None
        prev=None
        current=second
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        
        # merge the two list
        first = head
        second= prev
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2

        