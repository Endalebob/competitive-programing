class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_request = defaultdict(set)
        course_list = [0]*numCourses
        for course, pre_req in prerequisites:
            pre_request[pre_req].add(course)
            course_list[course] += 1
        deq = deque()
        ans = []
        for i in range(numCourses):
            if course_list[i] == 0:
                deq.append(i)
        while deq:
            current = deq.popleft()
            ans.append(current)
            for i in pre_request[current]:
                if course_list[i] > 0:
                    course_list[i] -= 1
                    if course_list[i] == 0:
                        deq.append(i)
        if len(ans) == numCourses:
            return ans
        return []