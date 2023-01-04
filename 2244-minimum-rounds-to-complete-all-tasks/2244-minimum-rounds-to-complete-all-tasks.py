class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        ans = 0
        for i in count:
            if count[i] == 1:
                return -1
            ans += ceil(count[i]/3)
        return ans