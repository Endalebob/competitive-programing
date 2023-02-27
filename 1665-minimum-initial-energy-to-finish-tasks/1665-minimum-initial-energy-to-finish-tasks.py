class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x : (-(x[1]-x[0]),-x[1]))
        ans = 0
        curr = 0
        for i in tasks:
            if curr < i[1]:
                ans += i[1]-curr
                curr = i[1]-i[0]
            else:
                curr -= i[0]
        return ans
            