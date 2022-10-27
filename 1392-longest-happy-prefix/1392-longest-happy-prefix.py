class Solution:
    def longestPrefix(self, s: str) -> str:
        def pattern_table(pattern):
            table = [0] * len(pattern)
            index = 1
            current_match = 0
            while index < len(pattern):
                if pattern[index] == pattern[current_match]:
                    current_match += 1
                    table[index] = current_match
                    index += 1
                else:
                    if current_match:
                        current_match = table[current_match - 1]
                    else:
                        current_match = 0
                        index += 1
            return table
        tab = pattern_table(s)
        i = len(s)-1
        ret = s[i-tab[i]+1:i+1]
        return ret

        