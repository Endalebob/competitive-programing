class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ''' 
        Our Goal is to construct the string by satisifying the constraint
        the constraint is string can't contain three consecutive letters.
        
        our goal is to construct the longest happy string. we need to use the character as much as possible. we start with the longest and soon. unitil there is no more.
        '''
        
        heap = [(-a,'a'),(-b,'b'),(-c,'c')]
        heapq.heapify(heap)
        ans = ''
        while heap:
            cnt,letter = heapq.heappop(heap)
            if len(ans) > 1 and ans[-2] == ans[-1] == letter:
                if heap:
                    cnt2,letter2 = heapq.heappop(heap)
                    if cnt2:
                        ans += letter2
                        if cnt2 < 0:
                            heapq.heappush(heap,(cnt2+1,letter2))
                        
                else:
                    return ans
            else:
                if cnt > -1:
                    return ans
                ans += letter
                cnt += 1
            if cnt< 0:
                heapq.heappush(heap,(cnt,letter))
        return ans
            