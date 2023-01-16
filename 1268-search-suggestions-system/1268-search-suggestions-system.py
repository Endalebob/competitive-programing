class Trie:
    def __init__(self):
        self.letters = {}
        self.end = False
    
    def insert(self,word):
        current = self
        for i in word:
            if i not in current.letters:
                current.letters[i] = Trie()
            current = current.letters[i]
        current.end = True
    
    def suggest(self,word):
        current = self
        for i in word:
            if i not in current.letters:
                return []
            current = current.letters[i]
        words = []
        def find(current,word):
            if len(words) >= 3:
                    return
            if current.end:
                words.append(word)
            letter = sorted(current.letters.keys())
            for i in letter:
                find(current.letters[i],word+i)
        find(current,word)
        return words[:3]
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for i in products:
            trie.insert(i)
        k = ''
        ans = []
        for i in searchWord:
            k += i
            ans.append(trie.suggest(k))
        return ans
        