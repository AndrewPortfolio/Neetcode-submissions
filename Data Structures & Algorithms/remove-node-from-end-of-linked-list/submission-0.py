# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy 
        right = head
        
        # want right pointer to be n amount of spaces in front of left
        k = 0
        while k < n:
            right = right.next
            k+=1

        #Go to the end of the list
        while right:
            right = right.next
            left = left.next
        
        target = left.next
        tmp = target.next
        target.next = None
        left.next = tmp     


        return dummy.next
