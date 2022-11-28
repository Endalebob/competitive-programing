class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = defaultdict(int)
        los = defaultdict(int)
        for i,j in matches:
            win[i] += 1
            los[j] += 1
        ans = [[],[]]
        for i in win:
            if i not in los:
                ans[0].append(i)
        for j in los:
            if los[j] == 1:
                ans[1].append(j)
        for i in ans:
            i.sort()
        return ans