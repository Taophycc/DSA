# Difficulty - EASY

from collections import deque
# class MyStack:

#     def __init__(self):
#         self.q = deque()
        

#     def push(self, x: int) -> None:
#         size = len(self.q)
#         self.q.append(x)
        
#         for _ in range(size):
#             frontElement = self.q.popleft()
#             self.q.append(frontElement)

#     def pop(self) -> int:
#         return self.q.popleft()    
        

#     def top(self) -> int:
#         return self.q[0]
        

#     def empty(self) -> bool:
#         return len(self.q)  == 0

#############
# Intuition
#############

# The problem asks us to implement a stack using only two queues. A stack is a Last-In, First-Out (LIFO) data structure, while a queue is a First-In, First-Out (FIFO) data structure. The main challenge is to simulate the LIFO behavior of a stack using FIFO queues.

# We can achieve this by ensuring that whenever an element is `push`ed onto the stack, it becomes the "first" element in the queue, effectively making it the next element to be `pop`ped.

# One common strategy is to use a single queue and rotate its elements during the `push` operation. When a new element is pushed, it's added to the back of the queue. Then, all elements that were previously in the queue are moved from the front to the back, one by one, until the newly added element is at the front. This way, the most recently pushed element is always at the front, ready to be popped.

# Walkthrough
# We will use a single `deque` (double-ended queue) from Python's `collections` module to simulate the queue.

# `__init__(self)`:
# 1. Initialize an empty `deque` called `self.q`.

# `push(self, x: int) -> None`:
# 1. Get the current `size` of the queue: `size = len(self.q)`.
# 2. Append the new element `x` to the right (back) of the queue: `self.q.append(x)`.
# 3. Now, to make `x` the front element (LIFO behavior), we need to move all `size` elements that were previously in the queue from their current positions to the back.
# 4. Loop `size` times:
#    a. Remove the element from the left (front) of the queue: `frontElement = self.q.popleft()`.
#    b. Append this `frontElement` to the right (back) of the queue: `self.q.append(frontElement)`.
#    After this loop, `x` will be at the front of the queue.

# `pop(self) -> int`:
# 1. Since `push` ensures the most recently added element is at the front, `pop` simply needs to remove and return the element from the left (front) of the queue: `return self.q.popleft()`.

# `top(self) -> int`:
# 1. The top element of the stack is always the front element of the queue. So, return the element at the left (front) of the queue without removing it: `return self.q[0]`.

# `empty(self) -> bool`:
# 1. Return `True` if the length of the queue is 0, `False` otherwise: `return len(self.q) == 0`.

# Example
# MyStack stack = new MyStack();
# stack.push(1);   // q: [1]
# stack.push(2);   // q: [2, 1] (after rotation)
# stack.top();     // returns 2
# stack.pop();     // returns 2, q: [1]
# stack.empty();   // returns false

# Let's trace `push(2)` when `q` is `[1]`:
# 1. `size = 1`
# 2. `self.q.append(2)` => `q: [1, 2]`
# 3. Loop `size` (1) time:
#    a. `frontElement = self.q.popleft()` => `frontElement = 1`, `q: [2]`
#    b. `self.q.append(frontElement)` => `self.q.append(1)` => `q: [2, 1]`
# Now, `2` is at the front, ready to be popped.

# Time Complexity:
# - `push`: O(N), where N is the number of elements in the stack. This is because we append the new element and then rotate all existing N elements.
# - `pop`: O(1), as it's a direct `popleft` operation.
# - `top`: O(1), as it's a direct access to the front element.
# - `empty`: O(1), as it's a direct length check.

# Space Complexity: O(N)
# The queue stores all N elements of the stack.