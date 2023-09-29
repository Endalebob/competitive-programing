class Trie:
    def __init__(self):
        self.letters = {}
        self.count = 0
    def insert(self,word):
        current = self
        for i in word:
            if i not in current.letters:
                current.letters[i] = Trie()
            current = current.letters[i]
            current.count += 1
    def find(self,word):
        current = self
        ans = 0
        for i in word:
            current = current.letters[i]
            ans += current.count
        return ans
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for i in words:
            trie.insert(i)
        ans = []
        for i in words:
            ans.append(trie.find(i))
        return ans
        