class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        s1Freq = {}
        s2Freq = {}
        s1Len = len(s1)
        for c in s1:
            s1Freq[c] = s1Freq.get(c, 0) + 1
        print(s1Freq)

        while r < len(s2):
            s2Freq[s2[r]] = s2Freq.get(s2[r], 0) + 1
            r += 1

            if l < r - s1Len:
                s2Freq[s2[l]] -= 1
                if s2Freq[s2[l]] == 0:
                    s2Freq.pop(s2[l])
                l += 1
            
            if s2Freq == s1Freq:
                return True

            
        return False
    
            


        