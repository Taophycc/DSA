# Difficulty - EASY

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(ch) for ch in s]

        while len(digits) > 2:
            newArr = []
            for i in range(len(digits) -1):
                mod = ((digits[i] + digits[i+1]) % 10)
                newArr.append(mod)
            digits = newArr  


        return digits[0] == digits[1]

'''
### Intuition

The problem asks us to repeatedly perform an operation on a string of digits until only two digits remain. The operation involves taking adjacent pairs of digits, summing them, and then taking the result modulo 10 to get a new digit. This new digit replaces the pair. We need to determine if the final two remaining digits are equal.

The core idea is to simulate this process directly. We can represent the digits as a list of integers. In each step of the `while` loop, we iterate through the current list of digits, calculate the sum modulo 10 for each adjacent pair, and store these new digits in a temporary list. After processing all pairs, this temporary list becomes the new `digits` list for the next iteration. This continues until the `digits` list contains only two elements. Finally, we compare these two remaining digits.

### Example Walkthrough

Let's consider an example, `s = "12345"`:

1.  **Initial:** `digits = [1, 2, 3, 4, 5]`

2.  **Iteration 1 (len(digits) = 5 > 2):**
    *   `newArr = []`
    *   `i = 0`: `digits[0] + digits[1] = 1 + 2 = 3`. `mod = 3 % 10 = 3`. `newArr = [3]`
    *   `i = 1`: `digits[1] + digits[2] = 2 + 3 = 5`. `mod = 5 % 10 = 5`. `newArr = [3, 5]`
    *   `i = 2`: `digits[2] + digits[3] = 3 + 4 = 7`. `mod = 7 % 10 = 7`. `newArr = [3, 5, 7]`
    *   `i = 3`: `digits[3] + digits[4] = 4 + 5 = 9`. `mod = 9 % 10 = 9`. `newArr = [3, 5, 7, 9]`
    *   `digits = newArr = [3, 5, 7, 9]`

3.  **Iteration 2 (len(digits) = 4 > 2):**
    *   `newArr = []`
    *   `i = 0`: `digits[0] + digits[1] = 3 + 5 = 8`. `mod = 8 % 10 = 8`. `newArr = [8]`
    *   `i = 1`: `digits[1] + digits[2] = 5 + 7 = 12`. `mod = 12 % 10 = 2`. `newArr = [8, 2]`
    *   `i = 2`: `digits[2] + digits[3] = 7 + 9 = 16`. `mod = 16 % 10 = 6`. `newArr = [8, 2, 6]`
    *   `digits = newArr = [8, 2, 6]`

4.  **Iteration 3 (len(digits) = 3 > 2):**
    *   `newArr = []`
    *   `i = 0`: `digits[0] + digits[1] = 8 + 2 = 10`. `mod = 10 % 10 = 0`. `newArr = [0]`
    *   `i = 1`: `digits[1] + digits[2] = 2 + 6 = 8`. `mod = 8 % 10 = 8`. `newArr = [0, 8]`
    *   `digits = newArr = [0, 8]`

5.  **Loop Termination:** `len(digits) = 2`, so the loop ends.

6.  **Return:** `digits[0] == digits[1]` which is `0 == 8`, which is `False`.

### Complexities

-   **Time Complexity:** Let `N` be the initial length of the string `s`.
    *   The outer `while` loop continues as long as `len(digits) > 2`. In each iteration, the length of `digits` decreases by 1. So, the `while` loop runs `N - 2` times.
    *   Inside the `while` loop, the `for` loop iterates `len(digits) - 1` times. In the first iteration, this is `N - 1` times, then `N - 2` times, and so on, until 2 times.
    *   The total number of operations is roughly the sum of an arithmetic series: `(N-1) + (N-2) + ... + 2`. This sum is approximately `O(N^2)`.
    *   Converting the string to a list of integers takes `O(N)` time.
    *   Therefore, the overall time complexity is **O(N^2)**.

-   **Space Complexity:**
    *   The `digits` list stores up to `N` integers.
    *   The `newArr` list also stores up to `N-1` integers.
    *   Therefore, the space complexity is **O(N)**.
'''