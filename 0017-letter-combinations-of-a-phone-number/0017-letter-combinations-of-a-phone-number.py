class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        strings = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        path = []

        buckets = []
        for char in digits:
            i = int(char) - 2
            buckets.append(strings[i])

        def backtrack(index):
            if index == len(buckets):
                res.append("".join(path))
                return

            current_bucket = buckets[index]

            for char in current_bucket:
                path.append(char)
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return res
            