class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        time_map = defaultdict(list)

        for name, time_str in zip(keyName, keyTime):
            hours, minutes = map(int, time_str.split(":"))
            total_minutes = hours * 60 + minutes

            time_map[name].append(total_minutes)

        ans = []
        for name, times in time_map.items():
            times.sort()

            for i in range(len(times) -2 ):
                if times[i+2] - times[i] <= 60:
                    ans.append(name)
                    break

        return sorted(ans)