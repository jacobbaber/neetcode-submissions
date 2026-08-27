class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        mostFreq = 0
        replacements = 0
        l = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            mostFreq = max(mostFreq, freq[s[r]])
            strLen = r - l + 1
            replacements = strLen - mostFreq
            while replacements > k:
                freq[s[l]] -= 1
                l += 1
                strLen = r - l + 1
                replacements = strLen - mostFreq
            res = max(res, r - l + 1)

        
        return res


            
            


            
        
        print(freq)
        