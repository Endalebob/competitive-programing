class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        'cbacdcbc'
        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i
        answer = ''
        i = 0
        visited = set()
        while i<len(s):
            if s[i] in visited:
                i += 1
                continue
            if last_index[s[i]] == i:
                answer += s[i]
                visited.add(s[i])
            else:
                j = i+1
                while s[j] in visited or (s[i] <= s[j] and last_index[s[j]] != j):
                    if s[j] in visited:
                        j += 1
                        continue
                    j += 1
                if s[j] >= s[i]:
                    answer += s[i]
                    visited.add(s[i])
                    
            i += 1
        return answer
                    
                    
        