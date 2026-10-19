class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        R, C = len(board) - 1, len(board[0]) - 1
        self.res = False
        self.seen = set()

        def dfs(x, y, wordSoFar):
            if wordSoFar == word or self.res == True:
                self.res = True
                return
            if x < 0 or x > C:
                return
            if y < 0 or y > R:
                return
            if (x,y) in self.seen:
                return

            wordSoFar += board[y][x]
            self.seen.add((x,y))
            
            dfs(x + 1, y, wordSoFar)
            dfs(x - 1, y, wordSoFar)
            dfs(x, y + 1, wordSoFar)
            dfs(x, y - 1, wordSoFar)

            self.seen.remove((x,y))

        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(c, r, "")
        return self.res

        




            

        
    
            



        