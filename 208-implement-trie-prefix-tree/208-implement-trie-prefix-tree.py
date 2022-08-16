class Node():
    def __init__(self):
        self.letters = {}
        self.isEnd = False
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for i in word:
            if i not in current.letters:
                current.letters[i] = Node()
            current = current.letters[i]
        current.isEnd = True

    def search(self, word: str) -> bool:
        current = self.root
        for i in word:
            if i not in current.letters:
                return False
            current = current.letters[i]
        return current.isEnd

    def startsWith(self, prefix: str) -> bool:
        current = self.root
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