# Difficulty - Medium

#    def reverseWords(s):
    
#     left = 0
#     right = len(s)-1
    
#     temp=""
#     ans=""
    
#     while left <= right:
#         ch = s[left]
#         if ch != ' ':
#             temp += ch
#         elif ch == ' ' and temp != '':
#             if ans!="": ans = temp + " " + ans
#             else: ans = temp
#             temp = ""
#         left += 1
    
#     if temp!="":
#         if ans!="": ans = temp + " " + ans
#         else: ans = temp
    
#     return ans

'''
### Intuition

The problem requires us to reverse the order of words in a string while handling multiple spaces and leading/trailing spaces. The final output should have single spaces between words and no extra spaces at the ends.

The core idea is to iterate through the string from left to right, build each word character by character, and then prepend each completed word to our result string. This way, the last word we process becomes the first word in our answer.

1.  We use a temporary string, `temp`, to accumulate the characters of the current word.
2.  As we iterate through the input string, if we encounter a non-space character, we append it to `temp`.
3.  When we hit a space, it signals the end of a word. If `temp` is not empty, we take the completed word from `temp` and prepend it to our final answer string, `ans`. We also add a space to separate it from the next word we prepend.
4.  After the loop finishes, there might be a final word held in `temp` (if the string doesn't end with a space). We need to make sure to prepend this last word to our `ans` as well.

This approach naturally handles the reversal of words and helps manage the spacing correctly.

### Example Walkthrough

Let's trace the example `s = "  hello world  "`:

1.  **Initialize:** `left = 0`, `temp = ""`, `ans = ""`.

2.  The loop starts. The first two characters are spaces, so `temp` remains empty.

3.  `left` is 2, `s[2]` is 'h'. `temp` becomes "h".
4.  ... a few iterations later ...
5.  `left` is 7, `s[7]` is a space. `temp` now holds "hello". Since `temp` is not empty, we update `ans`. `ans` is currently empty, so `ans` becomes "hello". We reset `temp` to `""`.

6.  `left` is 8, `s[8]` is 'w'. `temp` becomes "w".
7.  ... a few iterations later ...
8.  `left` is 13, `s[13]` is a space. `temp` holds "world". We update `ans`. `ans` is "hello", so we set `ans = temp + " " + ans`, which makes `ans` = "world hello". We reset `temp` to `""`.

9.  The loop continues until the end. The last characters are spaces, so no more words are formed.

10. The loop finishes. The final check for `temp` finds it empty.

11. **Return:** `ans`, which is "world hello".

### Complexities

-   **Time Complexity:** O(n), where n is the length of the input string. We iterate through the string once. While string concatenation in a loop can sometimes be inefficient, this approach is generally acceptable for typical constraints.
-   **Space Complexity:** O(n), as we use `ans` and `temp` strings, which in the worst case can store all the characters of the input string.
'''