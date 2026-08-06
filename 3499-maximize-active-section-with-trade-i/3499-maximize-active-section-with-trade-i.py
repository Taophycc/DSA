class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        st = list("1" + s + "1")
        max_gain = 0
        n = len(st)
        block = []
        cnt = 1

        for i in range(1, n):
            if st[i] == st[i-1]:
                cnt+=1
            else:
                block.append(cnt)
                cnt = 1
        block.append(cnt)

        for i in range(2, len(block)-1, 2):
            gain = block[i-1] + block[i+1]
            max_gain = max(max_gain, gain)
        return s.count("1") + max_gain

            
       
