class Node:
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
        for i in range(len(word)):
            if current.isEnd and i != len(word)-1 and word[i] == '/':
                return False
            current = current.letters[word[i]]
        return True

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for i in prefix:
            if i not in current.letters:
                return False
            current = current.letters[i]
        return True
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        word = Trie()
        for i in folder:
            word.insert(i)
        ans = []
        for i in folder:
            if word.search(i):
                ans.append(i)
        return ans
        