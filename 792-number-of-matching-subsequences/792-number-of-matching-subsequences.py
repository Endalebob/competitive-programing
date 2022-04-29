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

    def search(self, word, i) -> bool:
        current = self.root
        a = 0
        for c in i:
            if word[a] in current.letters:
                a += 1
            if a == len(word):
                return True
            current = current.letters[c]
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for i in prefix:
            if i not in current.letters:
                return False
            current = current.letters[i]
        return True
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word = defaultdict(list)
        ans = 0
        flag = False
        for i,v in enumerate(s): word[v].append(i)
        for i in words:
            limit = -1
            for j in i:
                flag = False
                for index in word[j]:
                    flag = False
                    if index>limit:
                        flag = True
                        limit = index
                        break
                if not flag:
                    break
            if flag:
                ans += 1
        return ans
                
        
        
            
                