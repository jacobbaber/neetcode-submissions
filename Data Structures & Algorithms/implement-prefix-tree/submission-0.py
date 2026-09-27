class PrefixTree:

    def __init__(self):
        self.tree = {}
         
        

    def insert(self, word: str) -> None:
            c = word[0]
            newWord = word[1:]
            if c not in self.tree:
                self.tree[c] = {}
            self.treeInsert(self.tree[c], newWord)
            
    def treeInsert(self, tree, word):
            if len(word) < 1:
                tree[None] = {None}
                return
            c = word[0]
            newWord = word[1:]
            if c not in tree:
                tree[c] = {}
            self.treeInsert(tree[c], newWord)
            



            


    def search(self, word: str) -> bool:
            c = word[0]
            newWord = word[1:]
            if c not in self.tree:
                return False
            return self.treeSearch(newWord, self.tree[c])
        
    
    def treeSearch(self, word, tree):
        if len(word) < 1 and None not in tree:
            return False
        elif len(word) < 1 and None in tree:
            return True
        
        c = word[0]
        newWord = word[1:]
        if c not in tree:

            return False
        return self.treeSearch(newWord, tree[c])


        

    def startsWith(self, prefix: str) -> bool:
        c = prefix[0]
        newWord = prefix[1:]
        if c not in self.tree:
            return False
        return self.treeStartsWith(newWord, self.tree[c])

    def treeStartsWith(self, word, tree):
        if len(word) < 1:
            return True
        
        c = word[0]
        newWord = word[1:]
        if c not in tree:
            return False

        return self.treeStartsWith(newWord, tree[c])
        
        