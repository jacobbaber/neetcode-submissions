class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        R, C = len(board) - 1, len(board[0]) - 1
        self.res = False
        self.seen = set()

        def dfs(x, y, i):
            if i == len(word) or self.res == True:
                self.res = True
                return
            if x < 0 or x > C:
                return
            if y < 0 or y > R:
                return
            if (x,y) in self.seen or board[y][x] != word[i]:
                return

            self.seen.add((x,y))
            
            dfs(x + 1, y, i + 1)
            dfs(x - 1, y, i + 1)
            dfs(x, y + 1, i + 1)
            dfs(x, y - 1, i + 1)

            self.seen.remove((x,y))

        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(c, r, 0)
        return self.res

        




            

        
    
            



        