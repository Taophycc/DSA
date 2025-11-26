# Difficulty - MEDIUM

def countPalindromicSubsequence(self, s: str) -> int:
    # create a set of unique chars in s to avoid redundancy
    unique_set = set(s)
    total_palindrome = 0

    # searching the unique characters saves us some lookup time
    for char in unique_set:
        # find the first kind of this char starting from the left
        first = s.find(char)
        # find the first kind of this char starting from the right
        last = s.rfind(char)

        # check if there's a space between them to ensure its a palindrome of len 3
        if last > first:
            # get the middle substring by slicing
            middle = s[first + 1 : last]
            # find the unique chars of middle
            # this tells us the number of unique palindrome we can have
            unique_char = len(set(middle))
            total_palindrome += unique_char

    return total_palindrome        

#############
# Explanation
#############

# Intuition
# We are looking for unique palindromic subsequences of length 3. A subsequence of length 3 is a palindrome if its first and last characters are the same (e.g., "a-a", "b-b"). The middle character can be anything. The problem asks for *unique* palindromes.

# A good strategy is to fix the outer characters of the palindrome. For example, if we choose 'a' as the outer character, we need to find the first 'a' and the last 'a' in the string. Any unique character between the first and last 'a' can serve as the middle character to form a unique palindrome.

# For example, in "a(bca)a", the first 'a' is at index 0 and the last is at index 4. The substring between them is "bca". The unique characters in "bca" are 'b', 'c', and 'a'. This means we can form three unique palindromes with 'a' as the outer character: "aba", "aca", and "aaa". We can repeat this process for every unique character in the alphabet ('a' through 'z').

# Walkthrough
# 1. Initialize a running total, `count`, to 0.
# 2. Create a set of the unique characters present in the input string `s`. This avoids redundant checks for characters that don't exist in the string.
# 3. Iterate through each `char` in this unique set. This `char` will be the potential outer character of our palindrome.
# 4. For each `char`, find its first occurrence (`first_idx`) and its last occurrence (`last_idx`) in the string `s`.
# 5. If `first_idx` is less than `last_idx`, it means the character appears at least twice, making a palindrome possible.
# 6. Consider the substring between these two indices: `s[first_idx + 1 : last_idx]`.
# 7. Find the number of unique characters within this middle substring. The length of the set of this substring gives us this count.
# 8. Add this number of unique characters to our running `count`. Each unique middle character forms a new unique length-3 palindrome with the outer `char`.
# 9. After iterating through all unique characters, `count` will hold the total number of unique length-3 palindromic subsequences. Return `count`.

# Walkthrough Example
# s = "aabca"
# 1. `count = 0`. Unique characters in `s` are {'a', 'b', 'c'}.
# 2. **char = 'a'**:
#    - `first_idx` of 'a' is 0.
#    - `last_idx` of 'a' is 4.
#    - `first_idx < last_idx` is true.
#    - Middle substring is `s[1:4]` which is "abc".
#    - Unique characters in "abc" are {'a', 'b', 'c'}. The count is 3.
#    - `count` becomes `0 + 3 = 3`. (Palindromes: "aaa", "aba", "aca")
# 3. **char = 'b'**:
#    - `first_idx` of 'b' is 2.
#    - `last_idx` of 'b' is 2.
#    - `first_idx < last_idx` is false. Do nothing.
# 4. **char = 'c'**:
#    - `first_idx` of 'c' is 3.
#    - `last_idx` of 'c' is 3.
#    - `first_idx < last_idx` is false. Do nothing.
# 5. Loop finishes. Return `count`, which is 3.

# Time Complexity: O(n)
# The outer loop runs for each unique character (at most 26 times, which is a constant). Inside the loop, `s.find()` and `s.rfind()` take O(n) time. Creating a set from the middle substring also takes O(n) in the worst case. Since the outer loop is a constant factor (at most 26), the total time complexity is O(26 * n), which simplifies to O(n).

# Space Complexity: O(1)
# We use a set to store the unique characters of the input string, which can be at most 26 for the English alphabet. The set for the middle substring also holds at most 26 characters. Therefore, the space used is constant.