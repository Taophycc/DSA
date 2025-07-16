// Difficulty - EASY
/*
function middleNode(head: ListNode | null): ListNode | null {
        if (head == null)
            return head

        let slow = head;
        let fast = head;

        while(fast.next !== null && fast.next.next !== null){
            slow = slow.next
            fast = fast.next.next
        }

        if(fast.next !== null){
            slow = slow.next
        }
            
        return slow
};
 */
