class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.pare = ""
        res = []


        def dfs(open, close):
            if len(self.pare) == n * 2:
                res.append(self.pare)
                return
            

            if open < n:
                self.pare += "("
                dfs(open + 1, close)
                self.pare = self.pare[:-1] 
            
            if close < open:
                self.pare += ")"
                dfs(open, close + 1)
                self.pare = self.pare[:-1]
        
        dfs(0,0)
        return res
            


        