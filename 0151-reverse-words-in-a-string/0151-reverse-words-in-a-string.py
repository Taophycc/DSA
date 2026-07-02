class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        left = 0
        res = []

        for right in range(n):
            # valid word
            if s[right] == " " :
                if s[left] != " ":
                    res.append(s[left:right])
                left = right + 1
            # cannot be a word: leading space
            # move left to right's spot
            elif s[left] == " ":
                left = right

        if left < n and s[left] != " ":
            res.append(s[left:])

        return " ".join(res[::-1])