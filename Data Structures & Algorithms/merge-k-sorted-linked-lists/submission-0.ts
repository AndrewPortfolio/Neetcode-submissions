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
     * @param {ListNode[]} lists
     * @return {ListNode}
     */
    mergeKLists(lists: ListNode[]): ListNode {
        if (!lists || lists.length === 0) {
            return null;
        }

        while (lists.length > 1) {
            let mergedLists = [];

            for (let i = 0; i < lists.length; i += 2) {
                let list1 = lists[i];
                let list2 = i+1 < lists.length ? lists[i+1] : null;

                mergedLists.push(this.mergeList(list1, list2));

            }
            lists = mergedLists;
        }
            return lists[0];
    }

    mergeList(l1: ListNode | null, l2: ListNode | null): ListNode {
        let dummy = new ListNode(0);
        let node = dummy;
        while (l1 !== null && l2 !== null) {
            if (l1.val < l2.val) {
                node.next = l1;
                l1 = l1.next
            } else {
                node.next = l2;
                l2 = l2.next;
            }
            node = node.next;
        }

        node.next = l1 || l2;

        return dummy.next;
    }
}
