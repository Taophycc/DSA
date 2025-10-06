# Difficulty - EASY

# def removeOuterParentheses(s):
#         opened = 0
#         result = ''
#         for ch in s:
#             if ch == '(':
#                 if (opened > 0):
#                     result += ch
#                 opened += 1
#             if ch == ')':
#                 if opened > 1:
#                     result += ch
#                 opened -= 1

#         return result 

'''
### Intuition

The problem asks us to remove the outermost parentheses of every "primitive" valid parentheses string within the input. A primitive string is a valid parentheses string that can't be split into two smaller non-empty valid parentheses strings.

The key insight is to track the nesting depth of the parentheses. We can iterate through the string and maintain a counter, let's call it `opened`.

- When we see an opening parenthesis `(`, we increment `opened`.
- When we see a closing parenthesis `)`, we decrement `opened`.

The outermost parentheses are the ones that enclose a primitive string.
- The first `(` of a primitive string is encountered when `opened` is 0. We should not include it.
- The last `)` of a primitive string is the one that makes `opened` become 0 again. We should not include it either.

So, we can build a result string by only appending parentheses that are not "outermost."
- We append an opening parenthesis `(` if `opened > 0` before we increment the counter.
- We append a closing parenthesis `)` if `opened > 1` before we decrement the counter.

### Example Walkthrough

Let's trace the example `s = "(()())(())"`:

1.  **Initialize:** `opened = 0`, `result = ""`

2.  `ch = '('`: `opened` is 0. This is an outermost `(`. We increment `opened` to 1.
3.  `ch = '('`: `opened` is 1. Since `opened > 0`, we append `(` to `result`. `result` is now `"("`. Increment `opened` to 2.
4.  `ch = ')'`: `opened` is 2. Since `opened > 1`, we append `)` to `result`. `result` is now `"()"`. Decrement `opened` to 1.
5.  `ch = '('`: `opened` is 1. Since `opened > 0`, we append `(` to `result`. `result` is now `"()("`. Increment `opened` to 2.
6.  `ch = ')'`: `opened` is 2. Since `opened > 1`, we append `)` to `result`. `result` is now `"()()"`. Decrement `opened` to 1.
7.  `ch = ')'`: `opened` is 1. This is an outermost `)`. We decrement `opened` to 0.

8.  `ch = '('`: `opened` is 0. This is an outermost `(`. We increment `opened` to 1.
9.  `ch = '('`: `opened` is 1. Since `opened > 0`, we append `(` to `result`. `result` is now `"()()("`. Increment `opened` to 2.
10. `ch = ')'`: `opened` is 2. Since `opened > 1`, we append `)` to `result`. `result` is now `"()()()"`. Decrement `opened` to 1.
11. `ch = ')'`: `opened` is 1. This is an outermost `)`. We decrement `opened` to 0.

The final `result` is `"()()()"`.

### Complexities

-   **Time Complexity:** O(n), where n is the length of the input string. We iterate through the string only once.
-   **Space Complexity:** O(n) in the worst case. The `result` string can grow up to the size of the input string.
'''