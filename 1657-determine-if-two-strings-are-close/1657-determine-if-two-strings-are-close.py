class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1,c2 = Counter(word1),Counter(word2)
        if sorted(c1.values()) != sorted(c2.values()) or sorted(c1.keys()) != sorted(c2.keys()):
            return False
        return True