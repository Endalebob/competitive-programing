class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dic = {}
        for i in range(len(arr)):
            if arr[i] in dic:
                dic[arr[i]].append(i)
            else:
                dic[arr[i]] = [i]
        dirr = [-1,1]
        length = len(arr)
        isValid = lambda l: 0<=l<length
        deq = deque()
        visted = set()
        deq.append([0,0])
        while deq:
            current = deq.popleft()
            if current[0] == length-1:
                return current[1]
            if current[0] not in visted:
                visted.add(current[0])
                for i in range(len(dic[arr[current[0]]])):
                    if dic[arr[current[0]]][-i-1] not in visted:
                        deq.append([dic[arr[current[0]]][-i-1],current[1]+1])
                        visted.add(dic[arr[current[0]]][-i-1])
            if isValid(current[0]+1) and current[0]+1 not in visted:
                deq.append([current[0]+1,current[1]+1])
            if isValid(current[0]-1) and current[0]-1 not in visted:
                deq.append([current[0]-1,current[1]+1])
