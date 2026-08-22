class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        bn = list(s)
        n = len(bn)
        seconds = 0
        made_swaps = True

        while made_swaps:
            made_swaps = False
            i = 0

            while i < n-1:
                if  bn[i] == "0" and bn[i+1] == "1":
                    bn[i] = "1"
                    bn[i+1] = "0"
                    made_swaps = True
                    i+=2
                else:
                    i+=1
            if made_swaps:
                seconds += 1

        return seconds



