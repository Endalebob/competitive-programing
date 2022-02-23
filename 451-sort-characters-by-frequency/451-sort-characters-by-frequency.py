class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = {}
        for char in s:
            if char in frequency: frequency[char] += 1
            else: frequency[char] = 1
                
        maxHeap = []
        heapq.heapify(maxHeap)
        for char in frequency: heapq.heappush(maxHeap,(-frequency[char],char))
        
        sortedChars = []
        while maxHeap:
            sortedChars.append(-maxHeap[0][0] * maxHeap[0][1])
            heapq.heappop(maxHeap)
        
        return "".join(sortedChars)