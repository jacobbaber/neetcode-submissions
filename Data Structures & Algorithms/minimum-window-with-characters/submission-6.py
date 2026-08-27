class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        tFreq = {}
        sFreq = {}


        currStr = ""
        for c in t:
            tFreq[c] = tFreq.get(c, 0) + 1

        keys = len(tFreq)

        

        while r < len(s):
            sFreq[s[r]] = sFreq.get(s[r], 0) + 1
            if sFreq[s[r]] == tFreq.get(s[r]):
                keys -= 1
            while keys == 0:
                if r - l + 1 < len(currStr) or currStr == "":
                    currStr = s[l:r+1]
                if sFreq[s[l]] == tFreq.get(s[l]):
                    keys += 1
                sFreq[s[l]] -= 1
                if sFreq[s[l]] == 0:
                    sFreq.pop(s[l])
                l += 1
            r += 1

        return currStr
                

        