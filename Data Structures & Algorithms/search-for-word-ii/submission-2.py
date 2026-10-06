class Trie:
    def __init__(self):
        self.isWord = False
        self.children = {}

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        ROW, COL = len(board), len(board[0])
        trie = Trie()
        self.visited = set()
        res = set()

        for word in words:
            trie.addWord(word)
        
        def dfs(r, c, node, wordSoFar):
            if r > ROW - 1 or c > COL - 1 or r < 0 or c < 0:
                return
            char = board[r][c]
            if char not in node.children or (r,c) in self.visited:
                return
            
        
            self.visited.add((r,c))
            wordSoFar += char

            node = node.children[char]
            if node.isWord == True:
                res.add(wordSoFar)
            

            dfs(r - 1, c, node, wordSoFar)
            dfs(r + 1, c, node, wordSoFar)
            dfs(r, c - 1, node, wordSoFar)
            dfs(r, c + 1, node, wordSoFar)

            self.visited.remove((r,c))

        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, trie, "")
        return list(res)



            
            






        
        