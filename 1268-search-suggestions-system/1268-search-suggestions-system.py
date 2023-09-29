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
    def suggestion(self,pre):
        current = self
        self.words = []
        for i in pre:
            if i not in current.letters:
                return []
            current = current.letters[i]
        self.dfs(current,pre)
        return self.words[:3]
    def dfs(self,current,word):
        if current.end:
            self.words.append(word)
        if len(self.words) >= 3:
                return
        letter = sorted(current.letters.keys())
        for i in letter:
            self.dfs(current.letters[i],word+i)
  
        
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        curr = ''
        for i in products:
            trie.insert(i)
        ans = []
        for i in searchWord:
            curr += i
            ans.append(trie.suggestion(curr))
        return ans
            
        