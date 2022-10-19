class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        the_same_frequency = defaultdict(list)
        keys = sorted(frequency.keys())
        for key in keys:
            the_same_frequency[frequency[key]].append(key)
        keys = sorted(the_same_frequency.keys(),reverse = True)
        ans = []
        for i in keys:
            for j in the_same_frequency[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans