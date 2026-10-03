class WordDictionary:

    def __init__(self):
        self.words = {}

        

    def addWord(self, word: str) -> None:
        words = self.words
        for c in word:
            if c not in words:
                words[c] = {}
            words = words[c]
        words['/'] = True


        return

        
        


    


        

    def search(self, word: str) -> bool:
        def dfs(i, words):
            if i == len(word):
                if '/' in words:
                    return True
                return False
            
            c = word[i]
            if c == '.':
                for key, child in words.items():
                    if key != '/' and  dfs(i + 1, child):
                        return True
                return False
            else:
                return c in words and dfs(i + 1, words[c])
            
        return dfs(0, self.words)


        
        
        
