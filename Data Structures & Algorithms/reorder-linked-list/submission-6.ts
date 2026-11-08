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
    /**
     * @param {ListNode} head
     * @return {void}
     */
    reorderList(head: ListNode | null): void {
        let slow = head;
        let fast = head.next;

        while (fast !== null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        // create 2nd half
        let second = slow.next;
        let prev = (slow.next = null);
        while (second !== null) {
            const tmp = second.next;
            second.next = prev;
            prev = second;
            second = tmp;
        }

        //connect the two halves
        let h1 = head;
        let h2 = prev;
        while (h1 !== null && h2 !== null) {
            let tmp1 = h1.next,
                tmp2 = h2.next;
            h1.next = h2;
            h2.next = tmp1;
            h1 = tmp1;
            h2 = tmp2;
        }

    }
}
