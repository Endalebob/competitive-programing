class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        one = students.count(1)
        zero = len(students)-one
        dic = {1:one,0:zero}
        students = deque(students)
        sandwiches=deque(sandwiches)
        while sandwiches and dic[sandwiches[0]]>0:
            if students[0] == sandwiches[0]:
                dic[students[0]] -= 1
                students.popleft()
                sandwiches.popleft()
            else:
                students.append(students.popleft())
        return len(students)