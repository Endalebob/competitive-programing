class RabinKarp:

    def __init__(self, patter, text, chr_len):
        self.pattern = patter
        self.text = text
        self.d = chr_len
        self.q = 10**9+7

    def search(self):
        m = len(self.pattern)
        n = len(self.text)
        if m>n:
            return -1

        hash_text = 0
        hash_pattern = 0
        h = 1

        for _ in range(m - 1):
            h = (h * self.d) % self.q

        for i in range(m):
            hash_pattern = (self.d * hash_pattern + ord(self.pattern[i])) % self.q
            hash_text = (self.d * hash_text + ord(self.text[i])) % self.q

        ans = -1
        for i in range(n - m + 1):

            if hash_text == hash_pattern:

                j = 0
                while j < m and self.text[i + j] == self.pattern[j]:
                    j += 1
                if j == m:
                    return i
            if i < n - m:
                hash_text = ((hash_text - ord(self.text[i]) * h) * self.d + ord(self.text[i + m])) % self.q
                if hash_text < 0:
                    hash_text += self.q
        return ans

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        find = RabinKarp(needle,haystack,26)
        return find.search()