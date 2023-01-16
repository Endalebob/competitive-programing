class Trie:

    def __init__(self):
        self.letters = {}
        self.end = False

    def insert(self, word: str) -> None:
        current = self
        for i in word:
            if i not in current.letters:
                current.letters[i] = Trie()
            current = current.letters[i]
        current.end = True

    def search(self, word: str) -> bool:
        current = self
        for i in word:
            if i not in current.letters:
                return False
            current = current.letters[i]
        return current.end
        

    def startsWith(self, prefix: str) -> bool:
        current = self
        for i in prefix:
            if i not in current.letters:
                return False
            current = current.letters[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)