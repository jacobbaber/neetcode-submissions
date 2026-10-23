class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col = set()
        negDiag = set()
        posDiag = set()

        

        def isValidRow(r):
            return "Q" not in matrix[r]
        def isValidCol(c):
            for r in range(n):
                if matrix[r][c] == "Q":
                    return False
            return True
        
        def isValidDiagonal(c, r):
            if (r - c) in negDiag or (r + c) in posDiag:
                return False
            return True
                        

        res = []
        matrix = ["" for r in range(n)]
        for r in range(len(matrix)):
            for i in range(n):
                matrix[r] += "."

        def dfs(r):
            if r == n:
                res.append(matrix.copy())
                return
            
            for c in range(n):
                if not (isValidRow(r) and isValidCol(c) and isValidDiagonal(c,r)):
                    continue
                
                matrix[r] = matrix[r][0:c] + "Q" + matrix[r][c + 1:]
                negDiag.add(r-c)
                posDiag.add(r + c)

                dfs(r + 1)

                matrix[r] = matrix[r][0:c] + "." + matrix[r][c + 1:]
                negDiag.remove(r-c)
                posDiag.remove(r + c)
        
        dfs(0)
        return res





        




        


    
        