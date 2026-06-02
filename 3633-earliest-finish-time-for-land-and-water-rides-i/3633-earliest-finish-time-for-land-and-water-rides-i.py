class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        res = float('Inf')

        for i in range(n):
            for j in range(m):
                finishTimeLand = landStartTime[i] + landDuration[i]
                boardTimeWater = max(finishTimeLand, waterStartTime[j])
                totalTimeLand = boardTimeWater + waterDuration[j]
                res = min(res, totalTimeLand)

                finishTimeWater = waterStartTime[j] + waterDuration[j]
                boardTimeLand = max(finishTimeWater, landStartTime[i])
                totalTimeWater = boardTimeLand + landDuration[i]
                res = min(res, totalTimeWater)
        return res
