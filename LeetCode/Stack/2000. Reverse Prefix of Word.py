# Difficulty - EASY

# def reversePrefix(self, word: str, ch: str) -> str:
#     stack = []

#     for char in word:
#         stack.append(char)
#         if char == ch:
#             break
#     if not stack or stack[-1] != ch:
#         return word
#     reversed_prefix = "".join(reversed(stack))
#     return reversed_prefix + word[len(stack):]

#############
# Intuition
#############

# The problem asks us to reverse the prefix of a given `word` up to the first occurrence of a specified character `ch`. If `ch` does not exist in the `word`, we should return the original `word`.

# We can iterate through the `word` character by character. As we iterate, we build up a prefix. Once we encounter the character `ch`, we know that this is the end of the prefix that needs to be reversed. We can then reverse this accumulated prefix and append the rest of the original word to it.

# A stack (or a list used as a stack) is a suitable data structure for building the prefix and then easily reversing it.

# Walkthrough
# 1. Initialize an empty list `stack`. This list will temporarily store the characters of the prefix.
# 2. Iterate through each `char` in the input `word`:
#    a. Append the current `char` to the `stack`.
#    b. If the current `char` is equal to `ch`, we have found the end of the prefix to be reversed. Break out of the loop.
# 3. After the loop, check two conditions:
#    a. If `stack` is empty, it means the `word` itself was empty, or the loop didn't run.
#    b. If `stack[-1]` (the last character added to the stack) is not `ch`, it means `ch` was not found in the `word`. In both these cases, no prefix needs to be reversed, so return the original `word`.
# 4. If `ch` was found, the `stack` now contains the characters of the prefix (including `ch`) in their original order. To reverse this prefix, we can use `reversed(stack)` and then `"".join()` to convert it back to a string. Store this in `reversed_prefix`.
# 5. The remaining part of the original `word` starts from the index right after the reversed prefix. This can be obtained using string slicing: `word[len(stack):]`.
# 6. Concatenate `reversed_prefix` and the remaining part of the `word`.
# 7. Return the combined string.

# Example
# word = "abcdefd", ch = "d"

# 1. stack = []
# 2. Iterate:
#    - char = 'a': stack = ['a']
#    - char = 'b': stack = ['a', 'b']
#    - char = 'c': stack = ['a', 'b', 'c']
#    - char = 'd': stack = ['a', 'b', 'c', 'd']. `char == ch` is True. Break.
# 3. Check conditions: `stack` is not empty, `stack[-1]` is 'd' (which is `ch`). Conditions pass.
# 4. `reversed_prefix = "".join(reversed(['a', 'b', 'c', 'd']))` => "dcba"
# 5. `word[len(stack):]` => `word[4:]` => "efd"
# 6. Return "dcba" + "efd" => "dcbaefd"

# Time Complexity: O(N)
# In the worst case, we iterate through the entire `word` once to find `ch` or to determine it's not present. String slicing and joining operations also take time proportional to the length of the string parts.

# Space Complexity: O(N)
# In the worst case, the `stack` could store all characters of the `word` if `ch` is the last character or not present. This makes the space complexity proportional to the length of the word.
