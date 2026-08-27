class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        while r < len(s2):
            currStr = s2[l:r+1]
            print(currStr)
            if sorted(s1) == sorted(currStr):
                return True
            r += 1
            l += 1
        return False
    
            


        