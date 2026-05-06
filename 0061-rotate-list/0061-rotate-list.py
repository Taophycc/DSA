# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
            
        curr = head
        length = 1

        while curr.next:
            curr = curr.next
            length += 1

        k = k % length
        if k == 0:
            return head
        
        steps_to_tail = length - k - 1
        newTail = head
        for _ in range(steps_to_tail):
            newTail = newTail.next

        newHead = newTail.next
        newTail.next = None
        curr.next = head
        return newHead

