class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
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
        k = len(a)*2
        past = a
        ans = int(len(b)/len(a))
        a = a*ans
        while len(a) <= k + len(b):
            find = search(a,b)
            if find != -1:
                return ans
            ans += 1
            a += past
        return -1
            
            