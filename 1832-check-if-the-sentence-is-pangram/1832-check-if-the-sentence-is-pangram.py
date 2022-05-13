class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        vstd = set()
        for i in sentence: vstd.add(i)
        return len(vstd) == 26