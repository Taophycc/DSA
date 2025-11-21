# Difficulty - MEDIUM

# def reorderList(head):
#     """
#     Do not return anything, modify head in-place instead.
#     """
#     if not head or not head.next:
#         return

#     # Step 1: Find the middle of the linked list
#     slow = fast = head
#     while fast.next and fast.next.next:
#         slow = slow.next
#         fast = fast.next.next

#     # Step 2: Split the list into two halves and reverse the second half
#     second = slow.next
#     slow.next = None  # Cut off the first half
    
#     prev = None
#     while second:
#         temp = second.next
#         second.next = prev
#         prev = second
#         second = temp

#     # The reversed second half now starts at `prev`
    
#     # Step 3: Merge the two halves
#     first = head
#     second = prev  # `prev` is the head of the reversed second half
#     while second:
#         # Store next pointers
#         temp1 = first.next
#         temp2 = second.next
        
#         # Link first half's node to second half's node
#         first.next = second
#         # Link second half's node to the original next of the first half
#         second.next = temp1
        
#         # Move pointers for the next iteration
#         first = temp1
#         second = temp2

###############
# Optimal
###############

# Intuition
# The goal is to reorder the list by interleaving the first half with the reversed second half.
# The process can be broken down into three main steps:
# 1. Find the middle of the linked list to split it into two halves.
# 2. Reverse the second half of the list.
# 3. Merge the first half and the reversed second half.

# Walkthrough
# 1. **Find the Middle:** We use the "slow and fast pointer" technique. The `slow` pointer moves one step at a time, while the `fast` pointer moves two steps. When the `fast` pointer reaches the end of the list, the `slow` pointer will be at the middle.
# 2. **Split and Reverse:**
#    - The list is split at the middle. The first half ends at `slow`, so we set `slow.next = None`.
#    - The second half starts right after `slow`. We reverse this second half using a standard iterative approach (with `prev`, `current`, and `temp` pointers).
# 3. **Merge:**
#    - We now have two lists: `first` (the original head) and `second` (the head of the reversed second half).
#    - We iterate while the `second` list is not empty, weaving the nodes together.
#    - In each step, we take the current `first` node, point its `next` to the current `second` node.
#    - Then, we point the `second` node's `next` to the original next of the `first` node (which we saved in a temporary variable).
#    - We then advance both `first` and `second` pointers to their next nodes for the subsequent merge step.

# Walkthrough Example
# head = 1 -> 2 -> 3 -> 4 -> 5
# 1. **Find Middle:** slow ends at 3, fast at 5. Middle is 3.
# 2. **Split & Reverse:**
#    - First half: 1 -> 2 -> 3. Second half: 4 -> 5.
#    - Set 3.next = None.
#    - Reverse 4 -> 5 to get 5 -> 4.
# 3. **Merge:**
#    - We have `first` = 1 -> 2 -> 3 and `second` = 5 -> 4.
#    - 1.next becomes 5. List: 1 -> 5 -> 2 -> 3.
#    - 5.next becomes 2. List: 1 -> 5 -> 2 -> 3.
#    - Advance `first` to 2, `second` to 4.
#    - 2.next becomes 4. List: 1 -> 5 -> 2 -> 4 -> 3.
#    - 4.next becomes 3. List: 1 -> 5 -> 2 -> 4 -> 3.
#    - Advance `first` to 3, `second` to None. Loop terminates.
# Final reordered list: 1 -> 5 -> 2 -> 4 -> 3.

# Time Complexity: O(n)
# - Finding the middle takes O(n).
# - Reversing the second half takes O(n/2), which is O(n).
# - Merging the two halves takes O(n/2), which is O(n).
# - The total time complexity is O(n).

# Space Complexity: O(1)
# The reordering is done in-place. We only use a few extra pointers, so the space complexity is constant.