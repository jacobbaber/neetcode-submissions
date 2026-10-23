class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        res = []
        self.comb = ""
        if len(digits) == 0:
            return []

        def dfs(i):
            if i >= len(digits): #2
                res.append(self.comb)
                return
            

            digit = int(digits[i])

            for c in letters[digit]:
                self.comb += c
                dfs(i + 1)
                self.comb = self.comb[:-1]
            
        dfs(0)
        return res

        