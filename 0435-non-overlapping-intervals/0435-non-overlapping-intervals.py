class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        intervals.sort(key=lambda x: x[1])

        cnt = 0
        last_end_time = float(-inf)

        for start_time, end_time in intervals:
            if start_time >= last_end_time:
                cnt+=1
                last_end_time = end_time
        return n - cnt