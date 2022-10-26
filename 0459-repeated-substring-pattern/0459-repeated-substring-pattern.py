class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
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


        def search(text,patter):
            table = pattern_table(patter)
            len_pattern = len(patter)
            len_text = len(text)
            if len_pattern > len_text:
                return -1
            i=j=0
            start_indexs = -1
            while i<len(text):
                if text[i] == patter[j]:
                    i += 1
                    j += 1
                if j == len_pattern:
                    return i-j
                elif i<len_text and text[i] != patter[j]:
                    if j != 0:
                        j = table[j-1]
                    else:
                        i += 1
            return start_indexs
        
        return search((s+s)[1:-1],s) != -1