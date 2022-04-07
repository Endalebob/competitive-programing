class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_request = defaultdict(set)
        
        course_list = []
        for course, pre_req in prerequisites:
            pre_request[pre_req].add(course)
        visited, cycle = set(),set()
        def dfs(i):
            if i in cycle:
                return False
            if i in visited:
                return True
            cycle.add(i)
            for j in pre_request[i]:
                if dfs(j) == False:
                    return False
            cycle.remove(i)
            visited.add(i)
            course_list.append(i)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return course_list[::-1]