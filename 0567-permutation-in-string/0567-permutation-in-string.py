class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Check if s2 contains a permutation of s1 using sliding window approach.
        
        Time Complexity: O(len(s1) + len(s2)) for initial setup and sliding window
        Space Complexity: O(1) - arrays of fixed size 26
        
        Algorithm:
        1. Use frequency arrays to count character occurrences
        2. Use a sliding window of size len(s1) over s2
        3. Track number of matching character frequencies between windows
        4. If all 26 letters match, we found a permutation
        """
        # Edge case: if s1 is longer than s2, no permutation can exist in s2
        if len(s1) > len(s2):
            return False
        # Initialize frequency arrays for 26 lowercase letters
        s1Count, s2Count = [0]*26, [0]*26

        # Build frequency count for s1 and the first window of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # Count how many of the 26 letters have matching frequencies
        # This optimization avoids comparing entire arrays repeatedly
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # Slide the window across s2
        l = 0
        for r in range(len(s1), len(s2)):
            # If all 26 characters match, we found a permutation
            if matches == 26: return True

            # Add the new character entering the window (right side)
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                # This character now matches, increment matches
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                # This character was matching before, but now exceeds count
                matches -= 1

            # Remove the character leaving the window (left side)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                # This character now matches after removal
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                # This character was matching before removal
                matches -= 1
            l += 1
        
        # Check the final window
        return matches == 26
        
