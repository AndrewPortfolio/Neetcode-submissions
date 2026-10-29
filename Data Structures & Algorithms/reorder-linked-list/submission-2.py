# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        #Find the half and end point of list 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse 2nd half
        second = slow.next
        slow.next = None
        prev = None     #new head of 2nd half
        while second: 
            tmp = second.next
            second.next = prev
            prev = second 
            second = tmp 
        
        list1 = head
        list2 = prev
        while list1 and list2:
            tmp1 = list1.next
            list1.next = list2 
            tmp2 = list2.next
            list2.next = tmp1
            list1 = tmp1 
            list2 = tmp2
        
            