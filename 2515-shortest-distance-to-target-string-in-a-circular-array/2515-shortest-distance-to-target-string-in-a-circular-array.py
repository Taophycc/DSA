class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # from the start index, calculate the shortest distance to reach a target
        # words[(i + 1) % n] for forward check
        # words[(i -1 + n) % n] backward check
        n = len(words)
        res = float('inf')
        for i in range(n):
            fIndex = (startIndex + i) % n
            if target == words[fIndex]:
                res = min(res, i)
        for i in range(n):
            bIndex = (startIndex - i + n) % n
            if target == words[bIndex]:
                res = min(res, i)
            
        return -1 if res == float('inf') else res
