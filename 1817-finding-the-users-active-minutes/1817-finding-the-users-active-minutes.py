class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic_id = defaultdict(set)
        dic_k = defaultdict(int)
        for i,j in logs:
            dic_id[i].add(j)
        for i in dic_id:
            dic_k[len(dic_id[i])] += 1
        return [dic_k[i] for i in range(1,k+1)]