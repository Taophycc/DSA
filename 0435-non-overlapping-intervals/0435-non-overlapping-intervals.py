class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        activities = []

        for i in range(n):
            activities.append((intervals[i][1], intervals[i][0], i))
        activities.sort()

        cnt = 0
        last_end_time = float(-inf)

        for end_time, start_time, index in activities:
            if start_time >= last_end_time:
                cnt+=1
                last_end_time = end_time
        return n - cnt