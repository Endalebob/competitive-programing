class Node:
    def __init__(self):
        self.letters = [None] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        val_of_a = ord('a')
        current = self.root

        for letter in word:
            letter = ord(letter) - val_of_a
            if current.letters[letter] is None:
                current.letters[letter] = Node()
            current = current.letters[letter]
        current.is_end = True

    def find(self, word):

        val_of_a = ord('a')
        current = self.root
        for letter in word:
            letter = ord(letter) - val_of_a
            if current.letters[letter] is None:
                return False
            current = current.letters[letter]

        return current.is_end

    def is_prefix(self, word):
        val_of_a = ord('a')
        current = self.root
        for letter in word:
            letter = ord(letter) - val_of_a
            if current.letters[letter] is None:
                return False
            current = current.letters[letter]

        return True

    def auto_complete(self, pref):
        val_of_a = ord('a')
        current = self.root

        for letter in pref:
            letter = ord(letter) - val_of_a
            if current.letters[letter] is None:
                return []
            current = current.letters[letter]

        words = []

        def dfs(current, pref):
            if current.is_end:
                words.append(pref)
            if len(words) >= 3:
                return
            if current is None:
                return
            for i in range(26):
                if len(words) >= 3:
                    return
                if current.letters[i]:
                    lett = chr(ord('a') + i)
                    dfs(current.letters[i], pref + lett)
        dfs(current,pref)

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
        