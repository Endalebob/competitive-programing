class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.calculated = []
        maximum = 0
        ans = 0
        dic = {}
        for i in self.persons:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            if maximum <= dic[i]:
                ans = i
                maximum = dic[i]
            self.calculated.append(ans)

    def q(self, t: int) -> int:

        right = len(self.persons)-1
        left = 0
        mid = (right + left)//2
        ans = right
        while left<right:
            if self.times[mid]<=t:
                left = mid + 1
                ans = mid
            elif self.times[mid] > t:
                right = mid
            mid = (right + left)//2
            if self.times[mid]<=t:
                ans = mid
        
        return self.calculated[ans]
