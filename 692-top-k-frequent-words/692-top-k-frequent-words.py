class Node:
    def __init__(self):
        self.letters = {}
        self.isEnd = False
        self.count = 0
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
        current.count += 1

    def search(self, word: str) -> bool:
        current = self.root
        for i in word:
            if i not in current.letters:
                return False
            current = current.letters[i]
        return current.count

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for i in prefix:
            if i not in current.letters:
                return False
            current = current.letters[i]
        return True

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word = Trie()
        ans = []
        count = defaultdict(set)
        for i in words: word.insert(i)
        for i in words: count[word.search(i)].add(i)
        keys = list(count.keys())
        keys.sort(reverse = True)
        for i in keys:      
            for j in sorted(count[i]):
                ans.append(j)
                if len(ans) == k:
                    return ans
        return ans
        
        