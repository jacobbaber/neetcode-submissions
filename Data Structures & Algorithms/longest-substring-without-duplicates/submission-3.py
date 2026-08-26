class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        maxLen = 0
        currStrHash = {}
        while r < len(s):
            if s[r] in currStrHash:
               while s[l] != s[r]:
                    currStrHash.pop(s[l])
                    l += 1
               l += 1

            else:
                maxLen = max(maxLen, r - l + 1)
                currStrHash[s[r]] = "1"
            
            r += 1
    
                    
        return maxLen






        