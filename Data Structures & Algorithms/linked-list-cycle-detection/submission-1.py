# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head 
        index = -1
        
        #track which nodes have been seen
        # {key:nodes index value: nodes val} 
        seen = {}

        i = 0
        while curr != None:
            if curr in seen:
                index = seen[curr]
                curr = None
                break
            
            seen[curr] = i
            curr = curr.next
            i +=1
        
        return index != -1 