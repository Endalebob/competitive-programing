class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        return ''.join(sorted(s,key = lambda a : (-freq[a],ord(a))))