class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes_list = []

        for time in timePoints:
            hours, minutes = time.split(":")
            total_minutes = int(hours) * 60 + int(minutes)
            minutes_list.append(total_minutes)

        minutes_list.sort()
        min_time = 1440 - minutes_list[-1] + minutes_list[0]

        for i in range(1, len(minutes_list)):
            diff = minutes_list[i] - minutes_list[i-1]
            min_time = min(min_time,diff)
        return min_time