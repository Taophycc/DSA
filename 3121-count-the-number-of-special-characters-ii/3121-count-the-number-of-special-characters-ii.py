class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_map = defaultdict(int)

        for char in word:
            lower_char = char.lower()

            if char.islower():
                if char_map[lower_char] == 0:
                    char_map[lower_char] = 1

                if char_map[lower_char] == 2:
                    char_map[lower_char] = -1

            elif char.isupper():
                if char_map[lower_char] == 0:
                    char_map[lower_char] = -1
                
                if char_map[lower_char] == 1:
                    char_map[lower_char] = 2

        cnt = 0
        for val in char_map.values():
            if val == 2:
                cnt += 1
        return cnt
