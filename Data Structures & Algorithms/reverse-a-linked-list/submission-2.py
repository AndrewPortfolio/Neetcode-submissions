# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 2 pointers: prev to the previous node
        # curr for the current node
        prev = None 
        curr = head

        # loop and reverse where each node is pointing to in list 
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp

        return prev
        
        