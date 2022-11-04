class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {}
        stack = []
        for i in range(len(speed)):
            dic[position[i]] = (target-position[i])/speed[i]
        position.sort()
        for i in position:
            while stack and stack[-1] <= dic[i]:
                stack.pop()
            stack.append(dic[i])
        return len(stack)
            
        