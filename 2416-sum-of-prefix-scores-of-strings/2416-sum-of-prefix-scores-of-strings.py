class Node:
    def __init__(self):
        self.letters = {}
        self.count = 0
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for i in word:
            if i not in current.letters:
                current.letters[i] = Node()
            # current.count += 1
            current = current.letters[i]
            current.count += 1

    def search(self, word: str) -> bool:
        current = self.root
        ans = 0
        for i in word:
            current = current.letters[i]
            ans += current.count
        return ans
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        dic = Trie()
        for i in words: dic.insert(i)
        return [dic.search(i) for i in words]