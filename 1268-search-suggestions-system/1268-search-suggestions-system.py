

    
class Solution:
    def __init__(self):
        self.letters = {}
        self.is_end = False


    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def insert(word):
            current = self
            for letter in word:
                if letter not in current.letters:
                    current.letters[letter] = Solution()
                current = current.letters[letter]
            current.is_end = True

        def auto_complete(pref):
            current = self
            for letter in pref:

                if letter not in current.letters:
                    return []
                current = current.letters[letter]

            words = []

            def dfs(current, pref):
                if current.is_end:
                    words.append(pref)
                letters = sorted(current.letters.keys())
                for letter in letters:
                    if len(words) >= 3:
                        return
                    dfs(current.letters[letter], pref + letter)

            dfs(current, pref)
            return words
        for product in products:
            insert(product)
        temp = ''
        ans = []
        for i in searchWord:
            temp += i
            ans.append(auto_complete(temp))
        return ans
        