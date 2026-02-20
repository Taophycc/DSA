class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 1
        arr = []
        res = 0
        start = 0
        for stop in range(1, n):
            if s[start] != s[stop]:
                start = stop
                arr.append(cnt)
                cnt = 1
            else:
                cnt += 1
        arr.append(cnt)

        for i in range(1, len(arr)):
            res += min(arr[i], arr[i-1])
        return res