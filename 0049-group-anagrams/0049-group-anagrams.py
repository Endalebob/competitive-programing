class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        same_group = defaultdict(list)
        for i in strs:
            same_group[tuple(sorted(i))].append(i)
        ans = []
        for i in same_group:
            ans.append(same_group[i])
        return ans