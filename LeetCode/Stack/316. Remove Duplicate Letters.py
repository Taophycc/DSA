# Difficulty - MEDIUM

# def removeDuplicateLetters(self, s: str) -> str:
#     stack = []
#     vis = set()
#     last = {c:i for i, c in enumerate(s)}

#     for i, c in enumerate(s):
#         if c in vis:
#             continue
        
#         while stack and stack[-1] > c and i < last[stack[-1]]:
#             vis.remove(stack.pop())

#         stack.append(c)
#         vis.add(c)    
#     return "".join(stack)

#############
# Intuition
#############

# The problem asks us to remove duplicate letters from a given string `s` such that the resulting string is the smallest in lexicographical order among all possible results. Each letter must appear exactly once.

# This problem can be solved using a monotonic stack. The key idea is to build the result string character by character, ensuring that at each step, we maintain the lexicographically smallest sequence.

# We need to consider two main conditions when deciding whether to keep a character or pop one from the stack:
# 1. **Lexicographical order:** If we encounter a character `c` that is smaller than the character at the top of our stack (`stack[-1]`), and `stack[-1]` appears again later in the string, we can potentially remove `stack[-1]` to get a lexicographically smaller result.
# 2. **Uniqueness:** Each character must appear exactly once in the final result. So, we cannot remove a character from the stack if it's the last occurrence of that character in the original string.

# To efficiently check the second condition, we can pre-compute the last occurrence index for each character in the string.

# Walkthrough
# 1. Initialize an empty list `stack` to build our result. This will act as a monotonic stack.
# 2. Initialize an empty set `vis` (visited) to keep track of characters already in our `stack`. This helps in ensuring uniqueness and avoiding redundant processing.
# 3. Create a dictionary `last` that stores the last occurrence index for each character in the input string `s`. This can be done by iterating through `s` once: `last = {c: i for i, c in enumerate(s)}`.

# 4. Iterate through the input string `s` with its index `i` and character `c`:
#    a. **Check if `c` is already in `vis`:** If `c` is already in `vis`, it means we have already processed this character and added it to our `stack` in an optimal position. So, we `continue` to the next character in `s`.
#    b. **Maintain monotonic stack:** While the `stack` is not empty, the character at the top of the `stack` (`stack[-1]`) is greater than the current character `c`, AND `stack[-1]` appears again later in the string (i.e., `i < last[stack[-1]]`):
#       - Remove `stack[-1]` from `vis` (because we are popping it from the stack).
#       - Pop `stack[-1]` from the `stack`.
#       This loop ensures that we remove larger characters from the stack if a smaller character `c` can replace them and the removed character will appear again later.
#    c. **Add current character to stack:** Append `c` to the `stack`.
#    d. **Mark as visited:** Add `c` to `vis`.

# 5. After iterating through all characters in `s`, the `stack` will contain the characters of the lexicographically smallest subsequence without duplicate letters.
# 6. Join the characters in the `stack` to form the final string and return it: `"".join(stack)`.

# Example
# s = "bcabc"

# Initial: stack = [], vis = set(), last = {'b': 3, 'c': 4, 'a': 2}

# 1. i = 0, c = 'b':
#    - 'b' not in vis.
#    - stack is empty.
#    - stack.append('b') => stack = ['b']
#    - vis.add('b') => vis = {'b'}

# 2. i = 1, c = 'c':
#    - 'c' not in vis.
#    - stack = ['b'], stack[-1] = 'b'. 'b' < 'c' is False.
#    - stack.append('c') => stack = ['b', 'c']
#    - vis.add('c') => vis = {'b', 'c'}

# 3. i = 2, c = 'a':
#    - 'a' not in vis.
#    - stack = ['b', 'c']. stack[-1] = 'c'. 'c' > 'a' is True. i (2) < last['c'] (4) is True.
#      - vis.remove('c') => vis = {'b'}
#      - stack.pop() => stack = ['b']
#    - stack = ['b']. stack[-1] = 'b'. 'b' > 'a' is True. i (2) < last['b'] (3) is True.
#      - vis.remove('b') => vis = set()
#      - stack.pop() => stack = []
#    - stack is empty. Loop ends.
#    - stack.append('a') => stack = ['a']
#    - vis.add('a') => vis = {'a'}

# 4. i = 3, c = 'b':
#    - 'b' not in vis.
#    - stack = ['a']. stack[-1] = 'a'. 'a' > 'b' is False.
#    - stack.append('b') => stack = ['a', 'b']
#    - vis.add('b') => vis = {'a', 'b'}

# 5. i = 4, c = 'c':
#    - 'c' not in vis.
#    - stack = ['a', 'b']. stack[-1] = 'b'. 'b' > 'c' is False.
#    - stack.append('c') => stack = ['a', 'b', 'c']
#    - vis.add('c') => vis = {'a', 'b', 'c'}

# Result: "".join(['a', 'b', 'c']) => "abc"

# Time Complexity: O(N)
# We iterate through the string `s` once. Each character is pushed onto the stack and popped from the stack at most once. Dictionary and set operations (lookup, insertion, deletion) take O(1) on average.

# Space Complexity: O(K)
# Where K is the number of unique characters in the string (at most 26 for lowercase English letters). The `stack`, `vis` set, and `last` dictionary will store at most K elements.
