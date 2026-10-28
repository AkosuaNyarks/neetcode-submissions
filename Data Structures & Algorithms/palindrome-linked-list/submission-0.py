# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        curr=slow
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        h1=head
        h2=prev
        while h2:
            if not h1 or not h1.next:
                return True
            if h1.val !=h2.val:
                return False
            h1=h1.next
            h2=h2.next
        return True

