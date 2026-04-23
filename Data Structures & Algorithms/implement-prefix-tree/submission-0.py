class PrefixTree:

    def __init__(self):
        self.children = {}
        self.is_end = False
        # Bug 1 fixed: no self.root here — the instance IS the root

    def insert(self, word: str) -> None:
        node = self          # start at the root (self)
        for i in word:
            if i not in self.children:   # Bug 3 fixed: node not self
                self.children[i] = PrefixTree()
            self = self.children[i]      # Bug 2 fixed: move node, not reassign children
        self.is_end = True

    def search(self, word: str) -> bool:

        for i in word:
            if i not in self.children:
                return False
            self = self.children[i]      # Bug 2 fixed: same pattern
        return self.is_end

    def startsWith(self, prefix: str) -> bool:
   
        for i in prefix:                 # Bug 4 fixed: prefix not word
            if i not in self.children:
                return False
            self = self.children[i]
        return True