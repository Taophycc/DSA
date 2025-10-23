# Difficulty - EASY

class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            res += abs(ord(s[i]) - ord(s[i-1]))
        return res

'''
### Intuition

The problem asks us to calculate the "score" of a string. The score is defined as the sum of the absolute differences between the ASCII values of adjacent characters in the string.

The approach is straightforward:
1.  Initialize a variable `res` (result) to 0. This variable will accumulate the score.
2.  Iterate through the string from the second character (index 1) up to the end.
3.  In each iteration, calculate the absolute difference between the ASCII value of the current character (`s[i]`) and the ASCII value of the previous character (`s[i-1]`). The `ord()` function in Python returns the ASCII value of a character.
4.  Add this absolute difference to `res`.
5.  After iterating through all adjacent pairs, `res` will hold the total score.

### Example Walkthrough

Let's consider the input `s = "hello"`:

1.  **Initialize:** `res = 0`

2.  **Iteration 1 (i = 1):**
    *   `s[1]` is 'e', `s[0]` is 'h'.
    *   `abs(ord('e') - ord('h')) = abs(101 - 104) = abs(-3) = 3`.
    *   `res = 0 + 3 = 3`.

3.  **Iteration 2 (i = 2):**
    *   `s[2]` is 'l', `s[1]` is 'e'.
    *   `abs(ord('l') - ord('e')) = abs(108 - 101) = abs(7) = 7`.
    *   `res = 3 + 7 = 10`.

4.  **Iteration 3 (i = 3):**
    *   `s[3]` is 'l', `s[2]` is 'l'.
    *   `abs(ord('l') - ord('l')) = abs(108 - 108) = abs(0) = 0`.
    *   `res = 10 + 0 = 10`.

5.  **Iteration 4 (i = 4):**
    *   `s[4]` is 'o', `s[3]` is 'l'.
    *   `abs(ord('o') - ord('l')) = abs(111 - 108) = abs(3) = 3`.
    *   `res = 10 + 3 = 13`.

6.  **Loop End:** The loop finishes.

7.  **Return:** `res = 13`.

### Complexities

-   **Time Complexity:** Let `N` be the length of the string `s`.
    *   We iterate through the string once from the second character to the end. This involves `N-1` operations.
    *   Each operation (accessing characters, `ord()`, `abs()`, addition) takes constant time.
    *   Therefore, the time complexity is **O(N)**.

-   **Space Complexity:**
    *   We only use a few variables (`res`, `i`) to store intermediate results. These take constant space.
    *   Therefore, the space Complexity is **O(1)**.
'''