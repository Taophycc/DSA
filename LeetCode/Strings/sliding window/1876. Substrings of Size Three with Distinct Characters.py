# Difficulty - EASY

#   def countGoodSubstrings(self, s: str) -> int:
#         n = len(s)
#         cnt = 0
#         # loop through the window
#         for i in range(n-2):
#             # check is the window is unique
#             if len(set(s[i:i+3])) == len(s[i:i+3]):
#                 cnt += 1

#         return cnt

"""
### Explanation:
The problem asks us to find the number of substrings of length three that have distinct characters.

1.  **Initialization**: We initialize a `count` variable to 0. This variable will store the number of "good" substrings found.

2.  **Iteration**: We iterate through the input string `s` using a `for` loop. The loop runs from `i = 0` up to `len(s) - 3`. This range is chosen because to form a substring of length three starting at index `i`, we need characters at `i`, `i+1`, and `i+2`. If `i` goes beyond `len(s) - 3`, we won't have enough characters remaining to form a substring of length three.

3.  **Extract Substring Characters**: Inside the loop, for each `i`, we extract the three characters that form the current substring: `s[i]`, `s[i+1]`, and `s[i+2]`.

4.  **Check for Distinct Characters**: We then check if these three characters are all distinct. This is done by comparing each pair of characters:
    *   `char1 != char2`
    *   `char1 != char3`
    *   `char2 != char3`
    If all three conditions are true, it means the characters are distinct.

5.  **Increment Count**: If the characters are distinct, we increment our `count` variable.

6.  **Return Result**: After iterating through all possible substrings of length three, the `count` variable will hold the total number of good substrings, which is then returned.

### Complexity

*   **Time Complexity**: O(N), where N is the length of the string `s`, because we iterate through the string once.
*   **Space Complexity**: O(1) because we are not using any extra space that scales with the input size.
"""