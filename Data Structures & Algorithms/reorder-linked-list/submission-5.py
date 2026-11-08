# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head 

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #create the 2nd half
        second = slow.next
        prev = slow.next = None 
        while second:
            tmp = second.next
            second.next = prev
            prev = second 
            second = tmp 
        
        #flip flop between halves
        half1 = head
        half2 = prev
        
        while half1 and half2:
            tmp1, tmp2 = half1.next, half2.next
            half1.next = half2
            half2.next = tmp1
            half1 = tmp1
            half2 = tmp2
