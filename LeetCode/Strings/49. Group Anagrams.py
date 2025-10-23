# Difficulty - MEDIUM

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groups = {}
#         for str_val in strs:
#             arr = [0]*26
#             for char in str_val:
#                 arr[ord(char) - ord('a')] += 1
            
#             key = tuple(arr)
#             if key in groups:
#                 groups[key].append(str_val)
#             else:
#                 groups[key] = [str_val]

#         return list(groups.values())

'''
### Intuition

The problem asks us to group words from a given list `strs` that are anagrams of each other. Anagrams are words that contain the same characters with the same frequencies, but in a different order. For example, "eat", "tea", and "ate" are anagrams.

The core idea to group anagrams is to find a canonical representation (a "key") for each word such that all anagrams have the same key, and non-anagrams have different keys. A common way to achieve this is by counting the frequency of each character in a word. Since the problem typically deals with lowercase English letters, we can use an array of size 26 to store the counts of 'a' through 'z'.

For each word:
1.  Initialize a count array (e.g., `[0]*26`).
2.  Iterate through the characters of the word and increment the count for the corresponding character in the array. For example, `ord(char) - ord('a')` gives the 0-indexed position for 'a' through 'z'.
3.  Convert this count array into an immutable key (e.g., a tuple) so it can be used as a dictionary key.
4.  Use a hash map (dictionary in Python) where the keys are these count tuples and the values are lists of words that share that count tuple (i.e., are anagrams).
5.  Finally, return all the values from the hash map.

### Example Walkthrough

Let's consider the input `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`:

1.  **Initialize:** `groups = {}`

2.  **Word: "eat"**
    *   `arr = [0]*26`
    *   'e': `arr[4] += 1`
    *   'a': `arr[0] += 1`
    *   't': `arr[19] += 1`
    *   `arr` becomes `[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]` (simplified for illustration)
    *   `key = tuple(arr)`
    *   `groups = {key_for_eat: ["eat"]}`

3.  **Word: "tea"**
    *   `arr` for "tea" will be the same as for "eat".
    *   `key = tuple(arr)` (same key as "eat")
    *   `key in groups` is true.
    *   `groups[key_for_eat].append("tea")`
    *   `groups = {key_for_eat: ["eat", "tea"]}`

4.  **Word: "tan"**
    *   `arr` for "tan": 't':1, 'a':1, 'n':1
    *   `key = tuple(arr)` (different key)
    *   `groups = {key_for_eat: ["eat", "tea"], key_for_tan: ["tan"]}`

5.  **Word: "ate"**
    *   `arr` for "ate" will be the same as for "eat".
    *   `key = tuple(arr)` (same key as "eat")
    *   `groups[key_for_eat].append("ate")`
    *   `groups = {key_for_eat: ["eat", "tea", "ate"], key_for_tan: ["tan"]}`

6.  **Word: "nat"**
    *   `arr` for "nat" will be the same as for "tan".
    *   `key = tuple(arr)` (same key as "tan")
    *   `groups[key_for_tan].append("nat")`
    *   `groups = {key_for_eat: ["eat", "tea", "ate"], key_for_tan: ["tan", "nat"]}`

7.  **Word: "bat"**
    *   `arr` for "bat": 'b':1, 'a':1, 't':1
    *   `key = tuple(arr)` (different key)
    *   `groups = {key_for_eat: ["eat", "tea", "ate"], key_for_tan: ["tan", "nat"], key_for_bat: ["bat"]}`

8.  **Return:** `list(groups.values())` which would be `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]` (order of inner lists and groups may vary).

### Complexities

-   **Time Complexity:** Let `N` be the number of strings in `strs` and `K` be the maximum length of a string in `strs`.
    *   For each string, we iterate through its characters to build the count array. This takes `O(K)` time.
    *   Converting the array to a tuple takes `O(26)` or `O(1)` time (since the array size is fixed).
    *   Dictionary operations (insertion and lookup) take `O(1)` on average.
    *   Since we do this for `N` strings, the total time complexity is **O(N * K)**.

-   **Space Complexity:**
    *   The `groups` dictionary stores all the words. In the worst case, if no words are anagrams, it stores `N` entries, each containing one word. If all words are anagrams, it stores one entry with `N` words. The total space for storing words is `O(N * K)`.
    *   Each key (the count array/tuple) takes `O(26)` or `O(1)` space.
    *   Therefore, the overall space complexity is **O(N * K)**.
'''