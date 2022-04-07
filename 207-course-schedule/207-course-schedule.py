class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_request = defaultdict(set)
        course_list = [0]*numCourses
        for course, pre_req in prerequisites:
            pre_request[pre_req].add(course)
            course_list[course] += 1
        deq = deque()
        for i in range(numCourses):
            if course_list[i] == 0:
                deq.append(i)
        while deq:
            current = deq.popleft()
            for i in pre_request[current]:
                course_list[i] -= 1
                if course_list[i] == 0:
                    deq.append(i)
        for i in course_list:
            if i != 0:
                return False
        return True
        