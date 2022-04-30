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
            current = current.letters[i]
            if not current.isEnd:
                return False
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        word = Trie()
        for i in words: word.insert(i)
        ans = ''
        for i in words:
            if word.search(i):
                if len(i)>len(ans):
                    ans = i
                elif len(i) == len(ans):
                    if i<ans:
                        ans = i
        return ans
        
        