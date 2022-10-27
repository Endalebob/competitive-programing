class ZAlgorithm:

    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.S = pattern + text

        self.z_table = [0] * len(self.S)

    def construct_table(self):
        self.z_table[0] = len(self.S)

        left = right = 0

        for k in range(1, len(self.S)):

            if k > right:
                n = 0

                while n + k < len(self.S) and self.S[n] == self.S[n + k]:
                    n += 1

                self.z_table[k] = n
                if n > 0:
                    left = k
                    right = k + n - 1

            else:

                p = k - left
                if self.z_table[p] < right - k + 1:
                    self.z_table[k] = self.z_table[p]
                else:
                    i = right + 1

                    while i < len(self.S) and self.S[i] == self.S[i - k]:
                        i += 1
                    self.z_table[k] = i - k
                    left = k
                    right = i - 1
        return sum(self.z_table)
class Solution:
    def sumScores(self, s: str) -> int:
        return ZAlgorithm(s,'').construct_table()