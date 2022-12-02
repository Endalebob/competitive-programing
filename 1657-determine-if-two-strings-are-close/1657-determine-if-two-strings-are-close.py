class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1,counter2 = Counter(word1),Counter(word2)
        if sorted(counter1.values()) != sorted(counter2.values()) or sorted(counter1.keys()) != sorted(counter2.keys()):
            return False
        return True