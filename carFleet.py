Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {}
        stack = []
        for i in range(len(speed)):
            dic[position[i]] = (target-position[i])/speed[i]
        position.sort()
        for i in position:
            while len(stack)>0 and stack[-1] <= dic[i]:
                stack.pop()
            stack.append(dic[i])
        return len(stack)