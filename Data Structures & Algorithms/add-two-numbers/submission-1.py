# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        dummy=ListNode(0)

        if not node
        return 0
                          c            c
        Input: l1 = [1,2,3], l2 = [4,5,6]
        res=0
        carry=0
        loop through each of the list:
        res=l1.val+l2.val+carry
        l1=l1.next
        l2=l2.next
        carry=res//10 //first digit
        value=res%10 //last digit
        dummy.next=value

        if l1:
            dummy.next=l1
        else:
            dummy.next=l2
        return dummy.next

        """


        # if not node:
        #     return 0
        dummy=ListNode(0)
        head=dummy

        res=0
        carry=0
        while l1 or l2 or carry:
            if l1:
                value1=l1.val
            else:
                value1=0
            if l2:
                value2=l2.val
            else:
                value2=0
            
            res=value1+value2+carry
            
            carry=res//10 #first digit
            last_digit=res%10
            dummy.next=ListNode(last_digit)
            dummy=dummy.next
            if l1:
                l1=l1.next
            else:
                 None
            if l2:
                l2=l2.next
            else:
                 None
        
        
        return head.next
        
        