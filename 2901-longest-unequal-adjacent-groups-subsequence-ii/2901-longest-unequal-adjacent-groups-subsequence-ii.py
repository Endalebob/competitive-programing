class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        @lru_cache(None)
        def hamming_dist(idx1,idx2):
            ham = 0
            for i in range(len(words[idx1])):
                if words[idx1][i] != words[idx2][i]:
                    ham += 1
                    if ham > 1:
                        return False
            return ham == 1
        memo = {}
        def dp(prev,j,ans):
            if (prev,j) in memo and memo[(prev,j)]>=len(ans):
                return
            memo[(prev,j)] = len(ans)
            if j == n:
                if len(ans) > len(self.ret):
                    self.ret = ans[:]
                return 
            if (groups[prev] != groups[j]) and (len(words[prev]) == len(words[j])) and hamming_dist(prev,j):
                ans.append(words[j])
                dp(j,j+1,ans)
                ans.pop()
                dp(prev,j+1,ans)
            else:
                dp(prev,j+1,ans)
        ans = [words[0]]
        self.ret = [words[0]]
        for i in range(n):
            temp = [words[i]]
            prev = i
            dp(i,i+1,temp)
        return self.ret
            
                
        