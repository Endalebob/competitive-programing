class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        limit = len(arr)
        isValid = lambda i: 0 <= i <limit
        checked = set()
        deq = deque()
        deq.append(start)
        while deq:
            current = deq.popleft()
            if arr[current] == 0:
                return True
            if isValid(current + arr[current]) and current + arr[current] not in checked:
                if arr[current + arr[current]] == 0:
                    return True
                deq.append(current + arr[current])
                checked.add(current + arr[current])
            if isValid(current - arr[current]) and current - arr[current] not in checked:
                if arr[current - arr[current]] == 0:
                    return True
                deq.append(current - arr[current])
                checked.add(current - arr[current])
        return False
            
                
            
            