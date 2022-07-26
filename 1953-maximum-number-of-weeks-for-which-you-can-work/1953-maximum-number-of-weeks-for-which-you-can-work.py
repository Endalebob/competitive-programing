class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        tot = sum(milestones)
        ans = 2*(tot-max(milestones))+1
        return min(ans,tot)