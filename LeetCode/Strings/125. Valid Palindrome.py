# Difficulty - EASY

# def isPalindrome(s: str):
#         left = 0
#         right = len(s) - 1

#         while left < right:
#             # Move left pointer to the next alphanumeric character
#             while left < right and not s[left].isalnum():
#                 left += 1 
#             # Move right pointer to the previous alphanumeric character
#             while left < right and not s[right].isalnum():    
#                 right -= 1
            
#             # Compare the characters (case-insensitive)
#             if s[left].lower() != s[right].lower():
#                 return False

#             # Move pointers inward
#             left += 1
#             right -= 1
            
#         return True

###############
# Optimal
###############

# Intuition
# A palindrome is a word, phrase, or sequence that reads the same backward as forward.
# To solve this, we can use a two-pointer approach. We'll have one pointer at the beginning of the string and another at the end.
# We'll move these pointers toward the center, comparing characters at each step while skipping non-alphanumeric characters.

# Walkthrough
# 1. Initialize two pointers, `left` at the start of the string (index 0) and `right` at the end (index n-1).
# 2. Use a `while` loop that continues as long as `left` is less than `right`.
# 3. Inside the loop, we first need to handle non-alphanumeric characters. We advance the `left` pointer until it points to an alphanumeric character.
# 4. Similarly, we move the `right` pointer backward until it points to an alphanumeric character.
# 5. Once both pointers are at valid characters, we compare them. To handle case-insensitivity, we convert both characters to lowercase before comparing.
# 6. If the characters are not equal, the string is not a palindrome, and we can immediately return `False`.
# 7. If they are equal, we move both pointers one step closer to the center (`left` moves right, `right` moves left).
# 8. If the loop completes without finding any mismatches, it means the string is a valid palindrome, and we return `True`.

# Walkthrough Example
# s = "A man, a plan, a canal: Panama"
# 1. left = 0 ('A'), right = 29 ('a'). 'A'.lower() == 'a'.lower(). They match. left becomes 1, right becomes 28.
# 2. left = 1 (' '), right = 28 ('m'). Skip ' ' at left. left becomes 2 ('m'). 'm'.lower() == 'm'.lower(). They match. left becomes 3, right becomes 27.
# 3. ...and so on.
# The pointers will continue to move inwards, comparing only the alphanumeric characters and ignoring case, until `left` is no longer less than `right`. Since all valid characters match, the function returns `True`.

# Time Complexity: O(n)
# In the worst case, we iterate through the entire string with both pointers, where n is the length of the string. Each character is visited at most once by each pointer.

# Space Complexity: O(1)
# We are not using any extra space that scales with the input size. The space used for the pointers is constant.