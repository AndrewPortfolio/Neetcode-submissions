/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    reorderList(head: ListNode | null): void {
        let slow = head;
        let fast = head; 

        // find the half and end of list 
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        // reverse the 2nd half
        let second = slow.next;
        let prev = null; // new head of 2nd half
        slow.next = null;
        while (second) {
            let tmp = second.next;
            second.next = prev;
            prev = second;
            second = tmp;
        }

        // link both halves together
        let list1 = head;
        let list2 = prev;
        while (list2) {
            let tmp1 = list1.next;
            list1.next = list2;
            let tmp2 = list2.next;
            list2.next = tmp1;
            list1 = tmp1;
            list2 = tmp2;
        }
    }
}