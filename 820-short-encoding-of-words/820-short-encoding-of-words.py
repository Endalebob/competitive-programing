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
        for i in word:
            if i not in current.letters:
                return False
            current = current.letters[i]
        if current.letters:
            return False
        return True

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        word = Trie()
        for i in words:
            word.insert(i[::-1])
        ans = 0
        for i in words:
            if word.search(i[::-1]):
                ans += (len(i)+1)
        return ans