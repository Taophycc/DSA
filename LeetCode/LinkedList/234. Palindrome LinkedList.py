# Difficulty - EASY

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def isPalindrome(head):
#     # use slow and fast pointers to find the middle of the linkedlist.
#     slow = fast = head 
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#     # reverse the second half of the linkedlist from middle to the end.
#     prev = None
#     curr = slow    
#     while curr:
#         next_node = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next_node

#     # The definition of a palindrome is that the first half of the sequence is a mirror image of the second half. so we compare the first half and the second half to see of they satisfy the condition for a valid palindrome. if yes True, else False
#     first_half = head
#     second_half = prev

#     is_Palindrome = True
#     while second_half:
#         if first_half.val != second_half.val:
#             is_Palindrome = False
#             break
#         first_half = first_half.next
#         second_half = second_half.next

#     return is_Palindrome

#############
# Intuition
#############

# A palindrome is a sequence that reads the same forwards and backward. For a linked list, this means the first half of the list should be a mirror image of the second half.

# The challenge with a linked list is that we can only traverse it in one direction. To compare the first half with the second half, we need to be able to traverse the second half in reverse.

# The overall strategy is:
# 1. Find the middle of the linked list.
# 2. Reverse the second half of the linked list.
# 3. Compare the first half with the reversed second half.

# Walkthrough
# 1. **Find the middle:** We use the slow and fast pointer technique. The `slow` pointer moves one step at a time, while the `fast` pointer moves two steps. When the `fast` pointer reaches the end of the list, the `slow` pointer will be at the middle.

# 2. **Reverse the second half:** Starting from the `slow` pointer (the middle), we reverse the rest of the list. We use a standard iterative approach with three pointers: `prev`, `curr`, and `next_node`. After this step, `prev` will be the head of the reversed second half.

# 3. **Compare the two halves:** We now have two pointers: `first_half` starting at the original `head` and `second_half` starting at `prev` (the head of the reversed second half). We iterate through both halves, comparing their values. If we find any mismatch, the list is not a palindrome. If we get through the entire second half without a mismatch, the list is a palindrome.

# Example
# head = [1, 2, 2, 1]

# 1. **Find middle:**
#    - slow at 1, fast at 1
#    - slow at 2, fast at 2
#    - slow at 2, fast at 1
#    - slow at 1, fast at None. Loop ends. `slow` is at the second '2'.

# 2. **Reverse second half:**
#    - The second half is [2, 1]. After reversing, it becomes [1, 2]. `prev` points to 1.

# 3. **Compare:**
#    - `first_half` is at the original head (1). `second_half` is at the new head of the reversed part (1).
#    - 1 == 1. Move both pointers.
#    - `first_half` is at 2. `second_half` is at 2.
#    - 2 == 2. Move both pointers.
#    - `second_half` is now None. The loop ends.

# Since there were no mismatches, the function returns `True`.

# Time Complexity: O(n)
# - Finding the middle takes O(n/2) which is O(n).
# - Reversing the second half takes O(n/2) which is O(n).
# - Comparing the two halves takes O(n/2) which is O(n).
# - The total time complexity is O(n).

# Space Complexity: O(1)
# We are modifying the list in-place and using only a few pointers. The space used is constant and does not scale with the size of the list.
