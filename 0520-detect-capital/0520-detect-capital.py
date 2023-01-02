class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt_cptl = 0
        for i in word:
            if i.isupper():
                cnt_cptl += 1
        if cnt_cptl:
            if cnt_cptl != len(word):
                if cnt_cptl != 1 or not word[0].isupper():
                    return False
        return True