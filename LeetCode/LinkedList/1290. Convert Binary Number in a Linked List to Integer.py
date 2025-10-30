# Difficulty - EASY

#    def getDecimalValue(self, head: Optional[ListNode]) -> int:
#         decimal_val = 0
#         temp = head

#         while temp is not None:
#             decimal_val = (decimal_val << 1) | temp.val
#             temp = temp.next

#         return decimal_val

'''
Intuition:
The problem asks us to convert a binary number represented as a linked list into an integer. The head of the linked list represents the most significant bit.
We can iterate through the linked list, and for each node, we can update the decimal value.
The core idea is to use bitwise operations for an efficient conversion. As we traverse the list, we can think of each node's value as a new bit to be added to our number.

Bit Shifting (`<<`):
We use the left bit shift operator `<<`. `decimal_val << 1` is equivalent to `decimal_val * 2`. It shifts the bits of `decimal_val` one position to the left, effectively multiplying it by 2. This makes space for the new bit from the current node.

Bitwise OR (`|`):
The bitwise OR operator `|` is used to set the new bit. `decimal_val | temp.val` is equivalent to `decimal_val + temp.val` in this case, since the last bit of `decimal_val` is now 0 after the left shift.

So, for each node, we first shift the current `decimal_val` to the left by one bit (`decimal_val << 1`) and then set the last bit to the current node's value using the bitwise OR operation (`| temp.val`).

Example Walkthrough:
Let's say the linked list is `1 -> 0 -> 1`.
1. Initialize `decimal_val = 0`.
2. First node is `1`. `decimal_val = (0 << 1) | 1 = 1`.
3. Second node is `0`. `decimal_val = (1 << 1) | 0 = 2`.
4. Third node is `1`. `decimal_val = (2 << 1) | 1 = 5`.
The linked list is now empty, so we return `decimal_val`, which is 5.

Time Complexity:
O(N), where N is the number of nodes in the linked list. We iterate through the linked list once.

Space Complexity:
O(1), as we are not using any extra space.
'''