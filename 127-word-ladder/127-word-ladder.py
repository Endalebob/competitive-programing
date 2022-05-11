class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = defaultdict(set)
        vstd = set()
        for i in wordList:
            for j in range(len(i)):
                temp = i[:j] + ' ' + i[j+1:]
                dic[temp].add(i)
        if endWord not in wordList:
            return 0
        hold = deque()
        hold.append((beginWord,1))
        while hold:
            current = hold.popleft()
            vstd.add(current[0])
            
            if endWord == current[0]:
                return current[1]
            for i in range(len(current[0])):
                temp = current[0][:i] + ' ' + current[0][i+1:]
                if temp in dic:
                    for j in dic[temp]:
                        if j not in vstd:
                            hold.append((j,current[1]+1))
        return 0