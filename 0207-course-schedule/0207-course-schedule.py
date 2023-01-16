class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        glb_flag = set()
        graph = defaultdict(list)
        for dep,ind in prerequisites:
            graph[ind].append(dep)
        
        def top_sort(node):
            if node in glb_flag:
                return True
            if node in lcl_flag:
                return False
            lcl_flag.add(node)
            for adj in graph[node]:
                if not top_sort(adj):
                    return False
            lcl_flag.remove(node)
            glb_flag.add(node)
            return True
        for i in range(numCourses):
            lcl_flag = set()
            if not top_sort(i):
                return False
        return True