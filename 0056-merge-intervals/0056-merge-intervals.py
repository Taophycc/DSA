class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return [[]]
        
        intervals.sort(key=lambda x: x[0])
        
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            curr_prev = res[-1][1]
            if curr_start <= curr_prev:
                res[-1][1] = max(curr_prev, curr_end)
            else:
                res.append([curr_start, curr_end])

        return res
