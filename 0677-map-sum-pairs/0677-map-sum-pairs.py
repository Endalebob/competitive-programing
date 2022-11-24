class Trie:
    def __init__(self):
        self.letters = {}
        self.is_end = False
    def insert(self,word):
        current = self
        for i in word:
            if i not in current.letters:
                current.letters[i] = Trie()
            current = current.letters[i]
        current.is_end = True
    
    def suggest(self,pref):
        current = self
        for letter in pref:
            if letter not in current.letters:
                return []
            current = current.letters[letter]

        words = []

        def dfs(current, pref):
            if current.is_end:
                words.append(pref)
            letters = current.letters.keys()
            for letter in letters:
                dfs(current.letters[letter], pref + letter)

        dfs(current, pref)
        return words
        
class MapSum:

    def __init__(self):
        self.dic = {}
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        if key not in self.dic:
            self.trie.insert(key)
        self.dic[key] = val

    def sum(self, prefix: str) -> int:
        keys = self.trie.suggest(prefix)
        ans = 0
        for i in keys:
            ans += self.dic[i]
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)