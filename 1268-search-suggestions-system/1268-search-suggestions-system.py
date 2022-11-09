class Trie:
    def __init__(self):
        self.letters = {}
        self.is_end = False

    def insert(self, word):
        current = self
        for letter in word:
            if letter not in current.letters:
                current.letters[letter] = Trie()
            current = current.letters[letter]
        current.is_end = True

    def search(self, word):
        current = self
        for letter in word:
            if letter not in current.letters:
                return False
            current = current.letters[letter]
        return current.is_end

    def prefix(self, pref):
        current = self
        for letter in pref:
            if letter not in current.letters:
                return False
            current = current.letters[letter]
        return True

    def auto_complete(self, pref):
        current = self
        for letter in pref:
            if letter not in current.letters:
                return []
            current = current.letters[letter]

        words = []

        def dfs(current, pref):
            if current.is_end:
                words.append(pref)
            for i in range(26):
                if len(words) >= 3:
                    return
                letter = chr(i + ord('a'))
                if letter in current.letters:
                    dfs(current.letters[letter], pref + letter)

        dfs(current, pref)
        return words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        temp = ''
        ans = []
        for i in searchWord:
            temp += i
            ans.append(trie.auto_complete(temp))
        return ans
        