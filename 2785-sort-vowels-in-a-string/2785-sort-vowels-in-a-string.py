class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a','A','e','E','o','O','u','U','i','I'}
        letters = []
        idx = []
        s = list(s)
        for l in range(len(s)):
            i = s[l]
            if i in vowels:
                letters.append(i)
                idx.append(l)
        letters.sort(key=lambda x: ord(x))
        for i in range(len(idx)):
            s[idx[i]] = letters[i]
        return ''.join(s)
        
        