# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        # offset curr from rem by n times
        while n > 0:
            curr = curr.next
            n -= 1

        #go to the end of the list to find the nth node
        while curr:
            curr = curr.next
            prev = prev.next
        
        prev.next = prev.next.next
        
        return dummy.next
