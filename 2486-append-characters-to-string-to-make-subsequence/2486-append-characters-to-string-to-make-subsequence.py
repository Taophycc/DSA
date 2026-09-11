class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        s_ptr, t_ptr = 0, 0

        while s_ptr < n and t_ptr < m:
            if s[s_ptr] == t[t_ptr]:
                t_ptr += 1
            s_ptr += 1

        return m - t_ptr
        