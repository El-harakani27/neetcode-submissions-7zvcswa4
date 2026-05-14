class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        
        for i in word:
            if i not in self.children:
                self.children[i] = WordDictionary()
            self = self.children[i]
        self.is_end = True
        

    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            curr = root
            for i in range(j,len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.is_end
        return dfs(0,self)
        
